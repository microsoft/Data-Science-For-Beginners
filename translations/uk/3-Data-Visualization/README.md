<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1441550a0d789796b2821e04f7f4cc94",
  "translation_date": "2025-08-30T18:39:17+00:00",
  "source_file": "3-Data-Visualization/README.md",
  "language_code": "uk"
}
-->
# Візуалізації

![бджола на квітці лаванди](../../../translated_images/bee.0aa1d91132b12e3a8994b9ca12816d05ce1642010d9b8be37f8d37365ba845cf.uk.jpg)
> Фото <a href="https://unsplash.com/@jenna2980?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Дженни Лі</a> на <a href="https://unsplash.com/s/photos/bees-in-a-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Візуалізація даних — одна з найважливіших задач для дата-сайєнтиста. Зображення варті тисячі слів, а візуалізація може допомогти вам виявити різноманітні цікаві аспекти ваших даних, такі як піки, аномалії, групування, тенденції та багато іншого, що допоможе вам зрозуміти історію, яку ваші дані намагаються розповісти.

У цих п'яти уроках ви дослідите дані, отримані з природи, і створите цікаві та красиві візуалізації, використовуючи різні техніки.

| Номер теми | Тема | Пов'язаний урок | Автор |
| :-----------: | :--: | :-----------: | :----: |
| 1. | Візуалізація кількостей | <ul> <li> [Python](09-visualization-quantities/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/09-visualization-quantities) </li> </ul>|<ul> <li> [Джен Лупер](https://twitter.com/jenlooper)</li><li> [Відуші Гупта](https://github.com/Vidushi-Gupta)</li> <li>[Жаслін Сонді](https://github.com/jasleen101010)</li></ul> |
| 2. | Візуалізація розподілу | <ul> <li> [Python](10-visualization-distributions/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/10-visualization-distributions) </li> </ul>|<ul> <li> [Джен Лупер](https://twitter.com/jenlooper)</li><li> [Відуші Гупта](https://github.com/Vidushi-Gupta)</li> <li>[Жаслін Сонді](https://github.com/jasleen101010)</li></ul> |
| 3. | Візуалізація пропорцій | <ul> <li> [Python](11-visualization-proportions/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Джен Лупер](https://twitter.com/jenlooper)</li><li> [Відуші Гупта](https://github.com/Vidushi-Gupta)</li> <li>[Жаслін Сонді](https://github.com/jasleen101010)</li></ul> |
| 4. | Візуалізація взаємозв'язків | <ul> <li> [Python](12-visualization-relationships/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Джен Лупер](https://twitter.com/jenlooper)</li><li> [Відуші Гупта](https://github.com/Vidushi-Gupta)</li> <li>[Жаслін Сонді](https://github.com/jasleen101010)</li></ul> |
| 5. | Створення змістовних візуалізацій | <ul> <li> [Python](13-meaningful-visualizations/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Джен Лупер](https://twitter.com/jenlooper)</li><li> [Відуші Гупта](https://github.com/Vidushi-Gupta)</li> <li>[Жаслін Сонді](https://github.com/jasleen101010)</li></ul> |

### Подяки

Ці уроки з візуалізації були написані з 🌸 [Джен Лупер](https://twitter.com/jenlooper), [Жаслін Сонді](https://github.com/jasleen101010) та [Відуші Гупта](https://github.com/Vidushi-Gupta).

🍯 Дані про виробництво меду в США взяті з проєкту Джессіки Лі на [Kaggle](https://www.kaggle.com/jessicali9530/honey-production). [Дані](https://usda.library.cornell.edu/concern/publications/rn301137d) отримані з [Департаменту сільського господарства США](https://www.nass.usda.gov/About_NASS/index.php).

🍄 Дані про гриби також взяті з [Kaggle](https://www.kaggle.com/hatterasdunton/mushroom-classification-updated-dataset), оновлені Хаттерасом Дантоном. Цей набір даних включає описи гіпотетичних зразків, що відповідають 23 видам пластинчастих грибів родини Agaricus і Lepiota. Гриби взяті з "Польового путівника грибів Північної Америки" (1981) від Audubon Society. Цей набір даних був переданий UCI ML 27 у 1987 році.

🦆 Дані про птахів Міннесоти взяті з [Kaggle](https://www.kaggle.com/hannahcollins/minnesota-birds), зібрані з [Wikipedia](https://en.wikipedia.org/wiki/List_of_birds_of_Minnesota) Ханною Коллінс.

Усі ці набори даних ліцензовані як [CC0: Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/).

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.