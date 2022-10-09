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

# -----------------------------------------------------------------------#

 ## AGGREGATING BRAZIL DATAFRAME

df_BR = dfAC.append([dfAL, dfAM, dfAP, dfBA, dfCE, dfDF, dfES, dfGO, dfMA, dfMG, dfMS, dfMT, \
                    dfPA, dfPB, dfPE, dfPI, dfPR, dfRJ, dfRN, dfRO, dfRR, dfRS, dfSE, dfSC, dfSP, dfTO, dfZZ])

df_BR_small = df_BR[['DS_CARGO_PERGUNTA','NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF','NR_ZONA','NR_SECAO',
                      'QT_VOTOS','NR_ZONA','QT_APTOS','QT_COMPARECIMENTO','QT_ABSTENCOES']]



# ---------------------- #
# |      CANDIDATE     | #
# |       RESULTS      | #
# ---------------------- #


# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - PRESIDENTIAL ELECTION

df_PRES = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Presidente')]

### COUNTRY LEVEL

dfPresCountry = df_PRES.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### STATE LEVEL

dfPresState = df_PRES.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfPresZona = df_PRES.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### SECTION LEVEL

dfPresSection = df_PRES.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA','NR_SECAO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()


# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - SENATE ELECTIION

df_SEN = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Senador')]

### STATE LEVEL

dfSENState = df_SEN.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfSENZona = df_SEN.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### SECTION LEVEL

dfSENSection = df_SEN.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA','NR_SECAO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - GOVERNOR ELECTIION

df_GOV = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Governador')]

### STATE LEVEL

dfGOVState = df_GOV.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfGOVZona = df_GOV.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### SECTION LEVEL

dfGOVSection = df_GOV.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA','NR_SECAO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - CONGRESS ELECTION

df_CON = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Federal')]

### STATE LEVEL

dfCONState = df_CON.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfCONZona = df_CON.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### SECTION LEVEL

dfCONSection = df_CON.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA','NR_SECAO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()



# -----------------------------------------------------------------------#

## DISPUTED POSITIONS RESULTS - STATE LEGISLATORS

df_SL = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Estadual') | (df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Distrital')]

### STATE LEVEL

dfSLState = df_SL.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfSLZona = df_SL.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### SECTION LEVEL

dfSLSection = df_SL.groupby(['NR_VOTAVEL','NM_VOTAVEL','NR_PARTIDO','NM_PARTIDO', 'SG_UF','NR_ZONA','NR_SECAO']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

# -----------------------------------------------------------------------#

# ---------------------- #
# |        PARTY       | #
# |       RESULTS      | #
# ---------------------- #


# -----------------------------------------------------------------------#

## PARTY RESULTS - CONGRESS

df_PARTY = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Federal')]

###STATE LEVEL

dfPARTYState = df_PARTY.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfPARTYZona = df_PARTY.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()


### SECTION LEVEL
dfPARTYSection = df_PARTY.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()



# -----------------------------------------------------------------------#

## PARTY RESULTS - STATE LEGISLATORS

df_PARTY_SL = df_BR_small[(df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Estadual') | (df_BR_small['DS_CARGO_PERGUNTA'] == 'Deputado Distrital')]

###STATE LEVEL

dfPARTY_SLState = df_PARTY_SL.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()

### ZONE LEVEL

dfPARTY_SLZona = df_PARTY_SL.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()


### SECTION LEVEL
dfPARTY_SLSection = df_PARTY_SL.groupby(['NR_PARTIDO','NM_PARTIDO','SG_UF']).agg({'QT_VOTOS': sum}) \
    .rename(columns={'QT_VOTOS': 'TOTAL_VOTOS' }).reset_index()



# -----------------------------------------------------------------------#


# -------  Below lines are optional if you want to create and download a .csv file ------ #

compression_opts = dict(method='zip',
                        archive_name='dfPresCountry.csv') 
dfPresCountry.to_csv('dfPresCountry.zip', index=False,
          compression=compression_opts) 

compression_opts = dict(method='zip',
                        archive_name='dfPresState.csv') 
dfPresState.to_csv('dfPresState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPresZona.csv') 
dfPresZona.to_csv('dfPresZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPresSection.csv') 
dfPresSection.to_csv('dfPresSection.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSENState.csv') 
dfSENState.to_csv('dfSENState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSENZona.csv') 
dfSENZona.to_csv('dfSENZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSENSection.csv') 
dfSENSection.to_csv('dfSENSection.zip', index=False,
          compression=compression_opts)

dfGOVState.to_csv('dfGOVState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfGOVZona.csv') 
dfGOVZona.to_csv('dfGOVZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfGOVSection.csv') 
dfGOVSection.to_csv('dfGOVSection.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfCONState.csv') 
dfCONState.to_csv('dfCONState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfCONZona.csv') 
dfSENZona.to_csv('dfCONZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfCONSection.csv') 
dfCONSection.to_csv('dfCONSection.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSLState.csv') 
dfSLState.to_csv('dfSLState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSLZona.csv') 
dfSLZona.to_csv('dfSLZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfSLSection.csv') 
dfSLSection.to_csv('dfSLSection.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTYState.csv') 
dfPARTYState.to_csv('dfPARTYState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTYZona.csv') 
dfPARTYZona.to_csv('dfPARTYZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTYSection.csv') 
dfPARTYSection.to_csv('dfPARTYSection.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTY_SLState.csv') 
dfPARTY_SLState.to_csv('dfPARTY_SLState.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTYZona.csv') 
dfPARTY_SLZona.to_csv('dfPARTY_SLZona.zip', index=False,
          compression=compression_opts)

compression_opts = dict(method='zip',
                        archive_name='dfPARTY_SLSection.csv') 
dfPARTY_SLSection.to_csv('dfPARTY_SLSection.zip', index=False,
          compression=compression_opts)

# -----------------------------------------------------------------------#




