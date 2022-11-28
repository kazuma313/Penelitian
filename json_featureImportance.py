from modul.olahFile import readFileExcel

importance = readFileExcel('data\FeatureImportance.xlsx')

featureImportance_dictionary = {
    "tertinggi" :
    {
        "gejala" : list(importance.nlargest(10,'score')['Gejala']),
        "nilai" : list(importance.nlargest(10,columns='score')['score'])
    },
    
    "terrendah" :
    {
        "gejala" : list(importance.nsmallest(10,'score')['Gejala']),
        "nilai" : list(importance.nsmallest(10,columns='score')['score'])
    }
}