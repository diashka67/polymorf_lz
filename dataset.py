import pandas as pd

class Payment:
    def __init__(self):
        self.data = None
        self.duplicates_delete = 0
        
        
     #мэджик метод лоя применения унарного минуса   
    def __neg__(self):
        self.duplicates_delete = self.data.duplicated().sum()
        self.data = self.data.drop_duplicates(keep='first')
        print(f"Количество повторяющихся строк в наборе данных: {self.duplicates_delete}")
        return self 
        
        
    # метода для фильтровки данных файла
    def sorting(self):
        self.data = pd.read_csv('var5.csv')

        #убираем дубликаты с файла
        -self
        
        #разделение датасета на два датасета
        filtered1_df = self.data[self.data['Место оплаты'] == 'Минск']
        filtered2_df = self.data[self.data['Место оплаты'] != 'Минск']
        
        print(filtered1_df)
        print(filtered2_df)
        
        #создание файлов после фильтровки
        filtered1_df.to_csv('output1.csv', index=False, encoding='utf-8')
        filtered2_df.to_csv('output2.csv', index=False, encoding='utf-8')
        
        
def main():
    pay = Payment()
    pay.sorting()


if __name__ == "__main__":
    main()
