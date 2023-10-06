# Триангуляция конуса

В данном репозитории находится проект на ReactJS (фронтенд) и Django REST Framework (бэкенд). Решается задача построения точек и нормалей конуса по формулам, а также отображение его на стороне клиента в соответствии с введенными данными. Для визуализации используется библиотека react-three-fiber. Бек лежит на платформе pythonanywhere, клиент лежит на github pages и доступен по [ссылке](https://harmonization.github.io/CAD-spa-triangulation/). 

Структура проекта:
- В папке static лежат статические файлы (css, sass, icon)
- В папке src лежат react компоненты
- В папке backend находится код django
- В папке backend/triangulation/Geometry реализована библиотека для вычисления точек и нормалей конуса на стороне сервера и используется в представлении: backend/triangulation/api/views.py

![1](Static/demo.png)
