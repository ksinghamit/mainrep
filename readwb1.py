import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt('WB_HCI.csv', delimiter=',', dtype=str, skip_header=0,usecols=np.arange(0,33))
# print('Shape: ',data1.shape)
# print('Size: ',data1.size)
# print('dimension: ',data1.ndim)

# ['STRUCTURE' 'STRUCTURE_ID' 'ACTION' 'FREQ' 'FREQ_LABEL' 'REF_AREA'
# 'REF_AREA_LABEL' 'INDICATOR' 'INDICATOR_LABEL' 'SEX' 'SEX_LABEL' 'AGE'
 # 'AGE_LABEL' 'URBANISATION' 'URBANISATION_LABEL' 'UNIT_MEASURE'
 # 'UNIT_MEASURE_LABEL' 'COMP_BREAKDOWN_1' 'COMP_BREAKDOWN_1_LABEL'
 # 'COMP_BREAKDOWN_2' 'COMP_BREAKDOWN_2_LABEL' 'COMP_BREAKDOWN_3'
 # 'COMP_BREAKDOWN_3_LABEL' 'TIME_PERIOD' 'OBS_VALUE' 'DATABASE_ID'
 # 'DATABASE_ID_LABEL' 'UNIT_MULT' 'UNIT_MULT_LABEL' 'UNIT_TYPE'
 # 'UNIT_TYPE_LABEL' 'TIME_FORMAT' 'TIME_FORMAT_LABEL']

#print(data1[:,6])

# #get unique list of countries
# c_str= np.char.strip(data1[:,6],'"')
# cntry_uniq = np.sort(np.unique(c_str))
# print('Countries: ',cntry_uniq)


# #get unique list of HCI indicators
# indi_str= np.char.strip(data1[:,8],'"')
# indi_uniq = np.sort(np.unique(indi_str))
# print('\nIndicators: ',indi_uniq)

# #get list of HCI indicator year
# hci_yr= data1[:,23]
# hci_yr_uniq = np.unique(hci_yr)
# hci_yr_only = hci_yr_uniq[np.char.isnumeric(hci_yr_uniq)]
# print('\nIndicator year: ',hci_yr_only)

# #get list of HCI indicator values
# hci_val= data1[:,24]
# print('\nIndicator value: ',hci_val)

#create an empty array to hold the hsci values for all countries from all years
asr_global = np.empty((data1.shape[0],8),dtype='U32')

#populate colums of country/region, hci indicator, year, hci_value, sex, unit, unit type
asr_global[:,0] = data1[:,6] #country

asr_global[:,1] = data1[:,7] #hci code
    
asr_global[:,2] = data1[:,8] # hci
    
asr_global[:,3] = data1[:,23] # year
    
asr_global[:,4] = data1[:,24] # hci value
    
asr_global[:,5] = data1[:,10] # sex

asr_global[:,6] = data1[:,16] # units
    
asr_global[:,7] = data1[:,30] # unit type


# create filter mask 
asr_2010_hci_mask = asr_global[:,1] == 'WB_HCI_ASR'
asr_2010_yr_mask = asr_global[:,3] == '2010'
asr_2010_sex = asr_global[:,5] == 'Male'

cntry_mask1 = asr_global[:,0] != 'High income'
    
cntry_mask2 = asr_global[:,0] != 'Low income'
    
cntry_mask3 = asr_global[:,0] != 'Lower middle income'
    
comb_mask = asr_2010_hci_mask & asr_2010_yr_mask & asr_2010_sex & cntry_mask1 & cntry_mask2 & cntry_mask3 #apply mask
    
filt_asr_2010 = asr_global[comb_mask]

#filter the values for the mask
filt_asr_2010_male = asr_global[comb_mask]



#print("Print values of adult male survival rate for 2010",filt_asr_2010_male)

#create bar chart
plt.bar(filt_asr_2010_male[:,0],filt_asr_2010_male[:,4])
plt.xlabel('Countries')
plt.ylabel('Adult Survival Rate')
plt.title('Global Adult Survival Rate (15 to 60 years)')
plt.show()
			
		
