def setup_import():
    global pd, np, plt, alldata, alldf, pys, jss, founds, corps, Asian_companies, US_companies, Apache, Huawei, IBM, Tencent, Eclipse, Google, Microsoft, Samsung, CNCF, Ecos
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import PercentFormatter
    
    pys = pd.read_csv('/Users/jaco/Desktop/Coding/Python/Scorecards_Analysis/pydata_final.csv')
    founds = pd.read_csv('/Users/jaco/Desktop/Coding/Python/Scorecards_Analysis/new_founds_final.csv')
    corps = pd.read_csv('/Users/jaco/Desktop/Coding/Python/Scorecards_Analysis/new_corps_final.csv')
    jss = pd.read_csv('/Users/jaco/Desktop/Coding/Python/Scorecards_Analysis/jss_final.csv')

    ### Add more datasets

    ### NOTE: manually cleaned data retroactively, so some cleaning lines ###d out


    alldata = [founds, corps, pys, jss]
    alld = pd.concat(alldata)
    alldf = pd.DataFrame(alld)

    ### Add remaining ecosystems to alldata list



    # pys = pd.read_csv('/Users/jaco/Desktop/Coding/Python/final_csvs/pydata.csv')
    # founds = pd.read_csv('/Users/jaco/Desktop/Coding/Python/final_csvs/founds.csv')
    # corps = pd.read_csv('/Users/jaco/Desktop/Coding/Python/final_csvs/corps.csv')
    # jss = pd.DataFrame(jss)

    alldf = pd.DataFrame(alldf)
    pys = pd.DataFrame(pys)
    corps = pd.DataFrame(corps)
    founds = pd.DataFrame(founds)


    # alldf = alldf.drop('Unnamed: 0', axis=1)
    # founds = founds.drop('Unnamed: 0', axis=1)
    # corps = corps.drop('Unnamed: 0', axis=1)
    # pys = pys.drop('Unnamed: 0', axis=1)


    # alldf.drop('Ecosystem', axis=1, inplace=True)

    all_languages = [pys, jss]
    all_lang = pd.concat(all_languages)
    Ecos = pd.DataFrame(all_lang)

    Huawei = alldf[alldf['Grouping']=='Huawei']
    Tencent = alldf[alldf['Grouping']=='Tencent']
    Google = alldf[alldf['Grouping']=='Google']
    Samsung = alldf[alldf['Grouping']=='Samsung']
    Microsoft = alldf[alldf['Grouping']=='Microsoft']
    Apache = alldf[alldf['Grouping']=='Apache']
    Eclipse = alldf[alldf['Grouping']=='Eclipse']
    CNCF = alldf[alldf['Grouping']=='CNCF']
    IBM = alldf[alldf['Grouping']=='IBM']

    Asia = [Huawei, Tencent, Samsung]
    Asian = pd.concat(Asia)
    Asian_companies = pd.DataFrame(Asian)
    China = [Huawei, Tencent]
    Chinese = pd.concat(China)
    Chinese_companies = pd.DataFrame(Chinese)
    USA = [Google, Microsoft]
    US = pd.concat(USA)
    US_companies = pd.DataFrame(US)


    # alldf.columns = ['Grouping', 'name', 'score', 'binary_artifacts', 'branch_protection', 'ci_tests',
    #              'cii_best_practices', 'code_review', 'contributors', 'dangerous_workflow',
    #             'dependency_update_tool', 'fuzzing', 'license', 'maintained', 'packaging',
    #             'pinned_dependencies', 'sast', 'security_policy', 'signed_releases',
    #             'token_permissions', 'vulnerabilities']

    # alldf = alldf.drop('webhooks', axis=1)
    # founds = founds.drop('webhooks', axis=1)
    # corps = corps.drop('webhooks', axis=1)
    # pys = pys.drop('webhooks', axis=1)
    # jss = jss.drop('webhooks', axis=1)
    alldf.sort_values('score', ascending=True)


    print("Setup complete.")

    # # print(jss)
setup_import()

# print(US_companies)
# print(IBM)

# pys.sort_values('binary-artifacts', ascending=True)
# print(founds['maintained'])

# print(corps['vulnerabilities'].mean())
# print(corps[corps.vulnerabilities < 10])

# print(Apache.mean())
