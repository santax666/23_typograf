# Typograf Service

Данный скрипт:
* создает и запускает веб-страницу на локальной станции пользователя по адресу http://localhost:5000/;
* выполняет функции Типографа - инструмента для подготовки русского текста к публикации в интернете;
* дает возможность дополнительного выбора опций при форматировании текста. Для этого необходимо выполнить 4 вещи:
    1. Написать функцию обработки текста и добавить её в файл [server.py][]. Функция должна принимать текст для обработки и возвращать отформатированный текст.
    2. Добавить пару (Название_опции: функция_форматирования) к словарю ***text_editing_functions***.
    3. В [шаблоне][] Типографа добавить блок с чекбоксом указанной функции
    
    ```
    <input type="checkbox" name="option_name" value=True id="fancy-checkbox-default" autocomplete="off" {{ 'checked' if 'option_name' in options }}/>
          <div class="btn-group">
            <label for="fancy-checkbox-default" class="btn btn-default">
              <span class="glyphicon glyphicon-ok"></span>
              <span> </span>
            </label>
            <label for="fancy-checkbox-default" class="btn btn-default active">
              Удалить/Отредактировать/Создать что-то..
            </label>
          </div>
    ```


    4. ВНИМАНИЕ! Название_опции в [шаблоне][] и в файле [server.py][] должно быть одинаковым!


## Запуск

Введите в терминале:

    python3 server.py

## Зависимости

Скрипт написан на языке Python 3, поэтому требует его наличия.

Для формирования и запуска веб-страницы должен быть установлен модуль [Flask][].

Базовый функционал Типографа использует модуль [chakert][], в связи с чем необходимо его наличие!

## Поддержка

Если у вас возникли сложности или вопросы по использованию скрипта, создайте 
[обсуждение][] в данном репозитории или напишите на электронную почту 
<IvanovVI87@gmail.com>.

## Документация

Документацию к модулю Flask можно получить по [ссылке1][].

Документацию к модулю chakert можно получить по [ссылке2][].

# Цели проекта

Данный код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)

[Flask]: https://pypi.python.org/pypi/Flask/0.12.2
[chakert]: https://pypi.python.org/pypi/chakert/0.2.1
[обсуждение]: https://github.com/santax666/23_typograf/issues
[ссылке1]: http://flask.pocoo.org/docs/0.11/quickstart/
[ссылке2]: https://github.com/Harut/chakert
[server.py]: ./server.py
[шаблоне]: ./templates/form.html
