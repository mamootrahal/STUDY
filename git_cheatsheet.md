# Git CLI Шпаргалка

## Настройка
git config --global user.name "Ваше Имя"
git config --global user.email "ваш@email"
git config --global init.defaultBranch main

## Создание и подключение
git init
git clone <url>
git remote add origin <url>
git remote -v

## Базовые действия
git status
git add <файл>
git add .
git commit -m "сообщение"
git log --oneline

## Отправка и получение
git push -u origin main
git push
git pull
git fetch

## Ветки
git branch
git branch <имя>
git checkout <имя>
git checkout -b <имя>
git merge <ветка>

## Отмена/правка
git restore <файл>
git reset HEAD <файл>
git commit --amend
git revert <hash>

## Синхронизация
git pull --rebase origin main
