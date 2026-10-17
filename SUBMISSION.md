# Перед сдачей лабораторной

Сам проект готов к публикации. Действия ниже требуют личного GitHub-аккаунта и партнёра по ревью, поэтому их нужно выполнить вручную.

## Опубликовать репозиторий

1. Создайте на GitHub публичный репозиторий `style-guide-project` без стартовых файлов.
2. Откройте терминал в этой папке и выполните:

   ```bash
   git init -b main
   git add .
   git commit -m "docs: create API documentation style guide"
   git remote add origin https://github.com/USERNAME/style-guide-project.git
   git push -u origin main
   ```

3. В **Settings → Actions → General → Workflow permissions** разрешите чтение и запись.
4. В **Settings → Pages** выберите публикацию из ветки `gh-pages`, каталог `/ (root)`.
5. Дождитесь зелёного workflow **Documentation**.

## Показать работу с ветками и PR

Чтобы история соответствовала пункту 11 задания, перенесите файл доступности в отдельный учебный коммит:

```bash
git switch -c docs/accessibility
git add docs/rules/accessibility.md mkdocs.yml
git commit -m "docs(accessibility): add accessible writing rules"
git push -u origin docs/accessibility
```

На GitHub создайте Pull Request в `main`. Попросите одногруппника оставить не менее трёх содержательных комментариев. Ответьте на замечания, внесите правки отдельным коммитом и после одобрения выполните **Squash and merge**.

> Если исходный коммит уже содержит `accessibility.md`, сначала публикуйте базовую версию без этого файла и соответствующей строки в `mkdocs.yml`, а затем верните их в ветке `docs/accessibility`.

## Что приложить к отчёту

- ссылку на репозиторий;
- ссылку на опубликованный сайт;
- ссылку на Pull Request;
- скриншот трёх комментариев ревью;
- скриншот успешного workflow и деплоя;
- имя рецензента.

Заполните персональные поля в конце страницы [«Отчёт по лабораторной»](docs/project/lab-report.md) перед сдачей.
