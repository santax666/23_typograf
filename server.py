from flask import Flask, render_template, request
from chakert import Typograph
from functools import reduce
import re


def delete_extra_line_breaks(text):
    text_new = re.sub('(\r\n){3,}', '\n\n', text)
    text_new = re.sub('(\r\n){2}', '\n', text_new)
    return text_new


def simple_replace_simbols(text):
    text_new = text
    string_for_replace = {'(c)': '©', '(C)': '©', '(с)': '©', '(С)': '©',
                          '(r)': '®', '(R)': '®', '(tm)': '™', '(TM)': '™',
                          'изза': 'из-за', 'изпод': 'из-под', '+-': '±',
                          '...': '…', '<=': '≤', '>=': '≥', '( ': '(',
                          'm2': 'm²', 'м2': 'м²', 'm3': 'm³', 'м3': 'м³',
                          '&quot;': '"', '&amp;': '&', '&lt;': '<', ' )': ')',
                          '&gt;': '>', '&circ;': 'ˆ', '&tilde;': '˜',
                          '&ndash;': '–', '&mdash;': '—', '&lsquo;': '‘',
                          '&rsquo;': '’', '&sbquo;': '‚', '&ldquo;': '“',
                          '&rdquo;': '”', '&bdquo;': '„', '&permil;': '‰',
                          '&lsaquo;': '‹', '&rsaquo;': '›', '&euro;': '€'}
    for old_value, new_value in string_for_replace.items():
        text_new = text_new.replace(old_value, new_value)
    return text_new


def replace_fractional_expressions(text):
    text_new = text
    pattern_for_replace = {'1/4': '¼', '1/2': '½', '3/4': '¾',
                           '1/7': '⅐', '1/9': '⅑', '1/10': '⅒',
                           '1/3': '⅓', '2/3': '⅔', '1/5': '⅕',
                           '2/5': '⅖', '3/5': '⅗', '4/5': '⅘',
                           '1/6': '⅙', '5/6': '⅚', '1/8': '⅛',
                           '3/8': '⅜', '5/8': '⅝', '7/8': '⅞', '0/3': '↉'}
    for old_value, new_value in pattern_for_replace.items():
        text_new = re.sub(r'\b{}\b'.format(old_value), new_value, text_new)
    return text_new


def get_active_options():
    text_editing_functions = {'breaks': delete_extra_line_breaks,
                              'typographics': simple_replace_simbols,
                              'fractions': replace_fractional_expressions}
    for option in text_editing_functions.keys():
        if not request.form.get(option, False):
            text_editing_functions[option] = False
    active_options = {k: v for k, v in text_editing_functions.items() if v}
    return active_options.keys(), active_options.values()


def typography_text(text, functions):
    text_new = reduce(lambda res, x: x(res), functions, text)
    return Typograph.typograph_text(text_new, lang='ru')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    options, functions = get_active_options()
    if request.method == 'GET':
        return render_template('form.html', disabled=True, options=options)
    else:
        text = request.form["text"]
        formatted_text = typography_text(text, functions)
        return render_template('form.html', old_text=text,
                               new_text=formatted_text, options=options)


if __name__ == "__main__":
    app.run()
