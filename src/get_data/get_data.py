import pandas as pd

class GetData:
    
    def __init__(self):
        pass
    
    def hello(self):
        print('Hello from GetData class')

    def get_data(self):
        """Reads data from data/raw and returns a pandas DataFrame"""
        df = pd.read_csv('../data/Air-pollution/number-of-deaths-by-risk-factor.csv')
        return df

    def rename_colums_data(self, df):
        """Renames columns from data/raw and returns a pandas DataFrame"""     
        return df.rename(columns={
            'Deaths - Cause: All causes - Risk: Outdoor air pollution - OWID - Sex: Both - Age: All Ages (Number)': 'Outdoor air pollution',
            'Deaths - Cause: All causes - Risk: High systolic blood pressure - Sex: Both - Age: All Ages (Number)': 'High systolic blood pressure',
            'Deaths - Cause: All causes - Risk: Diet high in sodium - Sex: Both - Age: All Ages (Number)': 'Diet high in sodium',
            'Deaths - Cause: All causes - Risk: Diet low in whole grains - Sex: Both - Age: All Ages (Number)': 'Diet low in whole grains',
            'Deaths - Cause: All causes - Risk: Alcohol use - Sex: Both - Age: All Ages (Number)': 'Alcohol use',
            'Deaths - Cause: All causes - Risk: Diet low in fruits - Sex: Both - Age: All Ages (Number)': 'Diet low in fruits',
            'Deaths - Cause: All causes - Risk: Unsafe water source - Sex: Both - Age: All Ages (Number)': 'Unsafe water source',
            'Deaths - Cause: All causes - Risk: Secondhand smoke - Sex: Both - Age: All Ages (Number)': 'Secondhand smoke',
            'Deaths - Cause: All causes - Risk: Low birth weight - Sex: Both - Age: All Ages (Number)': 'Low birth weight',
            'Deaths - Cause: All causes - Risk: Child wasting - Sex: Both - Age: All Ages (Number)': 'Child wasting',
            'Deaths - Cause: All causes - Risk: Unsafe sex - Sex: Both - Age: All Ages (Number)': 'Unsafe sex',
            'Deaths - Cause: All causes - Risk: Diet low in nuts and seeds - Sex: Both - Age: All Ages (Number)': 'Diet low in nuts and seeds',
            'Deaths - Cause: All causes - Risk: Household air pollution from solid fuels - Sex: Both - Age: All Ages (Number)': 'Household air pollution from solid fuels',
            'Deaths - Cause: All causes - Risk: Diet low in vegetables - Sex: Both - Age: All Ages (Number)': 'Diet low in vegetables',
            'Deaths - Cause: All causes - Risk: Low physical activity - Sex: Both - Age: All Ages (Number)': 'Low physical activity',
            'Deaths - Cause: All causes - Risk: Smoking - Sex: Both - Age: All Ages (Number)': 'Smoking',
            'Deaths - Cause: All causes - Risk: High fasting plasma glucose - Sex: Both - Age: All Ages (Number)': 'High fasting plasma glucose',
            'Deaths - Cause: All causes - Risk: Air pollution - Sex: Both - Age: All Ages (Number)': 'Air pollution',
            'Deaths - Cause: All causes - Risk: High body-mass index - Sex: Both - Age: All Ages (Number)': 'High body-mass index',
            'Deaths - Cause: All causes - Risk: Unsafe sanitation - Sex: Both - Age: All Ages (Number)': 'Unsafe sanitation',
            'Deaths - Cause: All causes - Risk: No access to handwashing facility - Sex: Both - Age: All Ages (Number)': 'No access to handwashing facility',
            'Deaths - Cause: All causes - Risk: Drug use - Sex: Both - Age: All Ages (Number)': 'Drug use',
            'Deaths - Cause: All causes - Risk: Low bone mineral density - Sex: Both - Age: All Ages (Number)': 'Low bone mineral density',
            'Deaths - Cause: All causes - Risk: Vitamin A deficiency - Sex: Both - Age: All Ages (Number)': 'Vitamin A deficiency',
            'Deaths - Cause: All causes - Risk: Child stunting - Sex: Both - Age: All Ages (Number)': 'Child stunting',
            'Deaths - Cause: All causes - Risk: Discontinued breastfeeding - Sex: Both - Age: All Ages (Number)': 'Discontinued breastfeeding',
            'Deaths - Cause: All causes - Risk: Non-exclusive breastfeeding - Sex: Both - Age: All Ages (Number)': 'Non-exclusive breastfeeding',
            'Deaths - Cause: All causes - Risk: Iron deficiency - Sex: Both - Age: All Ages (Number)': 'Iron deficiency',
        })
    
    def drop_columns_data(self, df):
        """Drops columns from data/raw and returns a pandas DataFrame"""
        return df.drop(columns=[
            'Code',
            'Low physical activity',
            'Non-exclusive breastfeeding',
            'Child wasting',
            'High systolic blood pressure',
            'High fasting plasma glucose',
            'Child stunting',
            'High body-mass index',
            'Secondhand smoke',
            'Diet low in fruits',
            'Diet high in sodium',
            'Drug use',
            'Household air pollution from solid fuels',
            'Low bone mineral density',
            'Smoking',
            'Vitamin A deficiency',
            'Unsafe sanitation',
            'Unsafe water source',
            'Diet low in vegetables',
            'Low birth weight',
            'Diet low in nuts and seeds',
            'Diet low in whole grains',
            'Alcohol use',
            'No access to handwashing facility',
            'Discontinued breastfeeding',
            'Iron deficiency',
            'Unsafe sex',
            'Outdoor air pollution'
        ])
    
    def filter_data(self, df, entity):
        """Filters data from data/raw and returns a pandas DataFrame"""
        return df[df['Entity'] == entity]
    

# if __name__ == '__main__':
#     hello()
