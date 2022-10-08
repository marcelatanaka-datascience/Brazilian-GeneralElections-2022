import pandas as pd

dfAC = pd.read_csv('bweb_1t_AC_051020221321.csv', encoding = 'Latin 1', sep=';')
dfAL = pd.read_csv('bweb_1t_AL_051020221321/bweb_1t_AL_051020221321.csv', encoding = 'Latin 1', sep=';')
dfAM = pd.read_csv('bweb_1t_AM_051020221321/bweb_1t_AM_051020221321.csv', encoding = 'Latin 1', sep=';')
dfAP = pd.read_csv('bweb_1t_AP_051020221321/bweb_1t_AP_051020221321.csv', encoding = 'Latin 1', sep=';')
dfBA = pd.read_csv('bweb_1t_BA_051020221321/bweb_1t_BA_051020221321.csv', encoding = 'Latin 1', sep=';')
dfCE = pd.read_csv('bweb_1t_CE_051020221321/bweb_1t_CE_051020221321.csv', encoding = 'Latin 1', sep=';')
dfDF = pd.read_csv('bweb_1t_DF_051020221321/bweb_1t_DF_051020221321.csv', encoding = 'Latin 1', sep=';')
dfES = pd.read_csv('bweb_1t_ES_051020221321/bweb_1t_ES_051020221321.csv', encoding = 'Latin 1', sep=';')
dfGO = pd.read_csv('bweb_1t_GO_051020221321/bweb_1t_GO_051020221321.csv', encoding = 'Latin 1', sep=';')
dfMA = pd.read_csv('bweb_1t_MA_051020221321/bweb_1t_MA_051020221321.csv', encoding = 'Latin 1', sep=';')
dfMG = pd.read_csv('bweb_1t_MG_051020221321/bweb_1t_MG_051020221321.csv', encoding = 'Latin 1', sep=';')
dfMS = pd.read_csv('bweb_1t_MS_051020221321/bweb_1t_MS_051020221321.csv', encoding = 'Latin 1', sep=';')
dfMT = pd.read_csv('bweb_1t_MT_051020221321/bweb_1t_MT_051020221321.csv', encoding = 'Latin 1', sep=';')
dfPA = pd.read_csv('bweb_1t_PA_051020221321/bweb_1t_PA_051020221321.csv', encoding = 'Latin 1', sep=';')
dfPB = pd.read_csv('bweb_1t_PB_051020221321/bweb_1t_PB_051020221321.csv', encoding = 'Latin 1', sep=';')
dfPE = pd.read_csv('bweb_1t_PE_051020221321/bweb_1t_PE_051020221321.csv', encoding = 'Latin 1', sep=';')
dfPI = pd.read_csv('bweb_1t_PI_051020221321/bweb_1t_PI_051020221321.csv', encoding = 'Latin 1', sep=';')
dfPR = pd.read_csv('bweb_1t_PR_051020221321/bweb_1t_PR_051020221321.csv', encoding = 'Latin 1', sep=';')
dfRJ = pd.read_csv('bweb_1t_RJ_051020221321/bweb_1t_RJ_051020221321.csv', encoding = 'Latin 1', sep=';')
dfRN = pd.read_csv('bweb_1t_RN_051020221321/bweb_1t_RN_051020221321.csv', encoding = 'Latin 1', sep=';')
dfRO = pd.read_csv('bweb_1t_RO_051020221321/bweb_1t_RO_051020221321.csv', encoding = 'Latin 1', sep=';')
dfRR = pd.read_csv('bweb_1t_RR_051020221321/bweb_1t_RR_051020221321.csv', encoding = 'Latin 1', sep=';')
dfRS = pd.read_csv('bweb_1t_RS_051020221321/bweb_1t_RS_051020221321.csv', encoding = 'Latin 1', sep=';')
dfSE = pd.read_csv('bweb_1t_SE_051020221321/bweb_1t_SE_051020221321.csv', encoding = 'Latin 1', sep=';')
dfSC = pd.read_csv('bweb_1t_SC_051020221321/bweb_1t_SC_051020221321.csv', encoding = 'Latin 1', sep=';')
dfSP = pd.read_csv('bweb_1t_SP_051020221321/bweb_1t_SP_051020221321.csv', encoding = 'Latin 1', sep=';')
dfTO = pd.read_csv('bweb_1t_TO_051020221321/bweb_1t_TO_051020221321.csv', encoding = 'Latin 1', sep=';')
dfZZ = pd.read_csv('bweb_1t_ZZ_051020221321/bweb_1t_ZZ_051020221321.csv', encoding = 'Latin 1', sep=';')



 ## AGGREGATING BRAZIL DATAFRAME

df_BR = dfAC.append([dfAL, dfAM, dfAP, dfBA, dfCE, dfDF, dfES, dfGO, dfMA, dfMG, dfMS, dfMT, \
                    dfPA, dfPB, dfPE, dfPI, dfPR, dfRJ, dfRN, dfRO, dfRR, dfRS, dfSE, dfSC, dfSP, dfTO, dfZZ])

df_BR_small = df_BR[['DS_CARGO_PERGUNTA','NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF','NR_ZONA','NR_SECAO',
                      'QT_VOTOS','NR_ZONA','QT_APTOS','QT_COMPARECIMENTO','QT_ABSTENCOES']]

# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - President

df_PRES = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Presidente')]

### COUNTRY LEVEL

dfPresCountry = df_PRES.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()




########## Below lines are optional if you want to create and download a .csv file ##########

compression_opts = dict(method='zip',
                        archive_name='dfPresCountry.csv') 
dfPresCountry.to_csv('dfPresCountry.zip', index=False,
          compression=compression_opts) 

########## ----------------------------------------------------------------------- ##########


