import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import warn
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from pandas.plotting import scatter_matrix

get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_columns', None)

def child_main():
    """
    Общий смысл
Функция child является вспомогательным инструментом быстрой проверки целесообразности того или иного исследования на имеющихся данных. Она строит регрессионную модель по указанным параметрам и выводит описательные статистики.
    Принцип работы
(1) Загрузка пользователем датасета по ссылке либо через прописанный путь. Возможные форматы: csv, dta, html, xlsx, json.
(2) Выбор зависимой и независимых переменных пользователем. Вывод таблицы с описательными статистиками и соответствующих графиков.
(3) Построение регрессионной модели с пакетом statsmodels. Вывод спецификации и  результата.
    Перед работой
Необходимые библиотеки: numpy, pandas, matplotlib, statsmodels, warnings, seaborn.
    Итог
Результатом работы функции является словарь со следующими ключами:

data - поданный на вход датасет;
descriptive - таблица с описательной статистикой по выбранным переменным;
new_data - датасет, состоящий из отобранных для модели переменных;
predictors - выбранные независимые переменные;
dependent - выбранная зависимая переменная;
specification - спецификация модели;
graph - визуализация описательных статистик;
model - регрессионная модель, построенная по указанным параметрам.

    """

    def downloader():

        def preprocesser(data):
            n = data.shape[0]
            
            for col in data.columns:
                if data[col].dtype == 'O':
                    n_cats = data[col].value_counts().shape[0]
                    dummy_decision = input(f'Предупреждение: переменная {col} является категориальной с {n_cats} категорий (всего {n} наблюдений). Удалить или преобразовать в дамми (1 - удалить, 2 - преобразовать в дамми)?\n')
                    
                    while dummy_decision not in ['1', '2']:
                        dummy_decision = input('Введите 1 или 2 (1 - удалить, 2 - преобразовать в дамми):\n')
                        
                    if dummy_decision == '2':
                        data = pd.get_dummies(data, columns=[col])
                        print(f'Предупреждение: переменная {col} трансформирована в дамми-переменные, т.к. принадлежит к типу object.\n')
                    else:
                        data.drop(columns=[col], inplace=True)
                        print(f'Предупреждение: переменная {col}, принадлежащая к типу object, удалена.\n')
                else:
                    pass
            
            naStats = data.isna().sum()
            
            if naStats.sum() > 0:
                naStats = naStats.to_dict()
                print('В ваших данных есть пропущенные значения. Перед анализом они будут исключены. Ознакомьтесь со статистикой:\n')
                _ = [print('Переменная %s имеет %d пропущенных значений.' % (ind, val)) for ind, val in naStats.items()]
            else:
                pass
                
            return data

        from urllib.error import HTTPError
        
        way = input('Введите ссылку, либо через запятую полный путь к Вашим данным и название файла: ').strip().split(', ')
        if len(way) > 1:
            way = way[0] + '/' + way[1]
        else:
            way = way[0]

        for i in way:
            if i in '\\':
                way = way.replace(i, '/')
            else:
                pass

        while True:
            try:
                while True:
                    if way[-3:] == 'csv':
                        data = pd.read_csv(way)
                        return preprocesser(data)
                    elif way[-3:] == 'dta':
                        data = pd.read_stata(way, convert_categoricals=False)
                        return preprocesser(data)
                    elif way[-3:] == 'tml':
                        data = pd.read_html(way)
                        return preprocesser(data)
                    elif way[-3:] == 'lsx':
                        data = pd.read_excel(way)
                        return preprocesser(data)
                    elif way[-3:] == 'son':
                        data = pd.read_json(way)
                        return preprocesser(data)
                    else:
                        way = input('Выбран некорректный формат файла. Введите файл с корректным форматом: ')
            except (HTTPError, OSError, FileNotFoundError) as e:
                way = input('Введенные Вами ссылка либо путь к файлу некорректны или подобный файл отсутствует в заявленной директории. Повторите ввод: ')


    def new_data_maker(data):
        def assign_your_dependent(data):
            while True:
                columns = ', '.join(list(data.columns))
                print(f'В Вашем датасете есть следующие переменные: {columns}.')
                print()
                dependent = input('Введите имя целевой переменной: ').strip()
                if dependent not in data.columns:
                    print('Целевая переменная с таким названием в датасете отсутствует. Проверьте и повторите ввод.')
                else:
                    return pd.DataFrame(data[dependent]), dependent

        def assign_your_predictors(data, dependent):
            while True:
                predictors = input('Введите через запятую имена предикторов: ').strip().split(', ')
                error = False
                for pred in predictors:
                        if pred not in data.columns:
                            error = True
                        else:
                            pass
                if len(set(predictors)) < len(predictors):
                    print('Значения переменных должны быть уникальными. Повторите ввод.')
                elif error == True:
                    print('Одна или несколько переменных с таким названием в датасете отсутствуют. Введите корректные имена.')
                elif dependent in predictors:
                    print('В Ваших предикторах содержится Ваша целевая переменная. Повторите ввод.')
                else:
                    print('Готово, Вы восхитительны!')
                    return pd.DataFrame(data[predictors]), predictors

        dep_data, dependent = assign_your_dependent(data)
        print()
        pred_data, predictors = assign_your_predictors(data, dependent)
        
        n = data.shape[0]
        n_preds = len(predictors)
        n_preds_recommended = n // 10
        
        if n_preds > n:
            warn('Количество предикторов (%d) больше, чем количество наблюдений (%d). Линейная модель не может быть оценена.' % (n_preds, n))
        elif n_preds == n:
            warn('Количество предикторов (%d) равно количеству наблюдений (%d). Оценки модели, скорее всего, неадекватны.' % (n_preds, n))
        elif n_preds < n and n_preds > n_preds_recommended:
            warn('Количество предикторов (%d) больше количества рекомендуемых (%d) для данного количество наблюдений (%d). Оценки модели могут быть неадекватными.' % (n_preds, n_preds_recommended, n))
        else:
            pass
        
        new_data = pd.concat([dep_data, pred_data], axis=1)

        return new_data.dropna(), predictors, dependent


    def descriptive_statistics(data):
        ans = input('Вывести на экран описательные статистики? (ответьте "да" или "нет") ').lower()
        if ans == 'да':
            print(data.describe())
            return data.describe()
        elif ans == 'нет':
            return data.describe()
        else:
            print('Ответьте "да" или "нет".')
            return descriptive_statistics(data)


    def specification(predictors, dependent):
        spec = dependent + ' ~ '
        for pred in predictors:
            if len(predictors) - predictors.index(pred) != 1:
                spec = spec + pred + ' + '
            else:
                spec += pred
        print(f'Спецификация Вашей модели: {spec.strip()}')
        return spec.strip()
    
    def correlation(data):
        ans = input('Вывести на экран матрицу корреляций? (ответьте "да" или "нет") \n').lower()
        dataCorr = data.corr().round(2)
        
        if ans == 'да':
            plt.figure(figsize=(15, 15))
            sns.heatmap(dataCorr, square=True, annot=True, linewidths=0.25)
            plt.title('Correlation matrix for numeric features')
            plt.show()
            return dataCorr
        elif ans == 'нет':
            return dataCorr
        else:
            print('Ответьте "да" или "нет".\n')
            return correlation(data)
        
        print(dataCorr)
        return dataCorr
    
    child = {}
    print('Приложение запущено...')
    print()

    data = downloader()
    child['data'] = data
    print()
    
    descriptive = descriptive_statistics(data)
    child['descriptive'] = descriptive
    print()
    
    new_data, predictors, dependent = new_data_maker(data)
    child['new_data'], child['predictors'], child['dependent'] = new_data, predictors, dependent
    print()
    
    corr = correlation(new_data)
    child['correlation'] = corr
    print()
    
    spec = specification(predictors, dependent)
    child['specification'] = spec
    print()
    
    graph = scatter_matrix(new_data, diagonal='hist', figsize=(10, 10), color='red',
                           edgecolor='grey', hist_kwds={'color':'yellow', 'edgecolor':'black'})
    child['graph'] = graph
    print()
    
    model = smf.ols(spec, data=new_data).fit()
    child['model'] = model
    print(f'Время насладиться выдачей: {model.summary()}')
    print()
        
    print('А теперь посмотрим на графики:')
    
    return child

child = child_main() 
