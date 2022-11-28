from modul.olahFile import readFileExcel

df_linear = readFileExcel('data\hasil_Linear.xlsx')
df_poly = readFileExcel('data\hasil_poly.xlsx')
df_rbf = readFileExcel('data\hasil_RBF.xlsx')
df_sigmoid = readFileExcel('data\hasil_sigmoid.xlsx')
df_split = readFileExcel('data\hasil_split0.xlsx')

data_dictionary = {
            "Linear" : 
                {
    
                        "PengaruhC" : 
                        {
                            "Akurasi" : df_linear[df_linear['Max_itter'] == 799]['Akurasi'].tolist(),
                            "C" : df_linear[df_linear['Max_itter'] == 799]['C'].tolist(),
                        },
    
                    
                     
                        "PengaruhMaxItter" :
                        {
                            "Akurasi": df_linear[(df_linear['C'] == 3.6)]['Akurasi'].tolist(),
                            "MaxItter": df_linear[(df_linear['C'] == 3.6)]['Max_itter'].tolist(),
                        },

                },
    
    
     
            "RBF" : 
                {
                
                        "PengaruhC" : 
                        {
                            "Akurasi" : df_rbf[(df_rbf['Max_itter'] == 799) & (df_rbf['Gamma'] == 'scale')]['Akurasi'].tolist(),
                            "C" : df_rbf[(df_rbf['Max_itter'] == 799) & (df_rbf['Gamma'] == 'scale')]['C'].tolist(),
                        },
                
                        "PengaruhMaxItter" :
                        {
                            "Akurasi" : df_rbf[(df_rbf['C'] == 3.6) & (df_rbf['Gamma'] == 'scale')]['Akurasi'].tolist(),
                            "MaxItter" : df_rbf[(df_rbf['C'] == 3.6) & (df_rbf['Gamma'] == 'scale')]['Max_itter'].tolist(),
                        },
                
                        "PengaruhGamma" :
                        {
                            "Akurasi" : df_rbf[(df_rbf['C'] == 3.6) & (df_rbf['Max_itter'] == 799) ]['Akurasi'].tolist(),
                            "Gamma" : df_rbf[(df_rbf['C'] == 3.6) & (df_rbf['Max_itter'] == 799)]['Gamma'].tolist(),           
                        },
                },
             
   
             "Poly" : 
                {
                     
                         "PengaruhC" : 
                         {
                             "Akurasi" : df_poly[(df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251)]['Akurasi'].tolist(),
                             "C" : df_poly[(df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251)]['C'].tolist(),
                         },
                         
                         "PengaruhMaxItter" :
                         {
                             "Akurasi" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251)]['Akurasi'].tolist(),
                             "MaxItter" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251) ]['Max_itter'].tolist(),
                         },
                         
                         "PengaruhGamma" :
                         {
                             "Akurasi" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251)]['Akurasi'].tolist(),
                             "Gamma" :  df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Coef0'] == 1) & (df_poly['Degree'] == 251)]['Gamma'].tolist(),
                         },
                    
                         "PengaruhCoef0" :
                         {
                             "Akurasi" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Degree'] == 251)]['Akurasi'].tolist(),
                             "Coef0" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Degree'] == 251)]['Coef0'].tolist(),
                             
                         },
                
                         "PengaruhDegree" :
                         {
                             "Akurasi" : df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) ]['Akurasi'].tolist(),
                             "Degree" :  df_poly[(df_poly['C'] == 3.6) & (df_poly['Max_itter'] == 799) & (df_poly['Gamma'] == 'scale') & (df_poly['Coef0'] == 1) ]['Degree'].tolist(),
                         },
                },
                 
   
             "Sigmoid" : 
                {
                 
                        "PengaruhC":
                        {
                            "Akurasi" : df_sigmoid[(df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Gamma'] == 'scale') & (df_sigmoid['Coef0'] == 1)]['Akurasi'].tolist(),
                            "C" :  df_sigmoid[(df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Gamma'] == 'scale') & (df_sigmoid['Coef0'] == 1)]['C'].tolist(),
                        },
                        
                        
                        "PengaruhMaxItter" :
                        {
                            "Akurasi" :  df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Gamma'] == 'scale') & (df_sigmoid['Coef0'] == 1)]['Akurasi'].tolist(),
                            "MaxItter" : df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Gamma'] == 'scale') & (df_sigmoid['Coef0'] == 1)]['Max_itter'].tolist(),
                        },
                        
                        "PengaruhGamma" :
                        {
                            "Akurasi" :  df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Coef0'] == 1)]['Akurasi'].tolist(),
                            "Gamma" : df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Coef0'] == 1)]['Gamma'].tolist(),
                        },
                        
                        "PengaruhCoef0" :
                        {
                            "Akurasi" : df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Gamma'] == 'scale') ]['Akurasi'].tolist(),
                            "Degree" : df_sigmoid[(df_sigmoid['C'] == 3.6) & (df_sigmoid['Max_itter'] == 799) & (df_sigmoid['Gamma'] == 'scale')]['Coef0'].tolist(),
                        },
                        
                
                },

                "Split" : {
                    "Akurasi" : df_split['Akurasi'].to_list(),
                    "DataTest" : df_split['dataTest'].to_list()
                }
             
        }