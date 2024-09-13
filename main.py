from flask import Flask, render_template, request

# Создаем экземпляр Flask приложения
app = Flask(__name__)


# Определяем маршрут для корневого URL
@app.route('/', methods=['GET', 'POST'])
def form():
    user_data = None  # Переменная для хранения данных о пользователе, введенных в форму
    if request.method == 'POST':  # Проверяем, была ли форма отправлена (метод POST)
        # Получаем данные из формы
        name = request.form.get('name')  # Получаем имя пользователя
        city = request.form.get('city')  # Получаем город
        hobby = request.form.get('hobby')  # Получаем хобби
        age = request.form.get('age')  # Получаем возраст

        # Сохраняем собранные данные в словаре
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

    # Рендерим шаблон form.html, передавая в него данные пользователя
    return render_template('form.html', user_data=user_data)


# Запускаем приложение, если скрипт выполняется напрямую
if __name__ == '__main__':
    app.run(debug=True)  # debug=True включает режим отладки для деталей ошибок