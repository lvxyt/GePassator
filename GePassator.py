┌─╼[~]
└────╼ cat /bin/passgen                  
#!/bin/bash

# Скрипт генератор паролей GePassator + параметры запуска

echo
echo     Генератор паролей GePassator с параметрами запуска
echo
echo ∗    Генерировать полностью случайные пароли
echo ∗    Включить хотя бы один номер в пароле
echo ∗    Включить хотя бы одну заглавную букву в пароле
echo ∗    Не включать двусмысленные символы в пароле
echo
read -p "⏵ Введите кол-во символов для пароля: " number
echo ──────────────────────╼
GePassator -1sncB "$number" 10
echo ──────────────────────╼