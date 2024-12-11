import pandas as pd
import os
# Define the Loan Performance table headers and data types
lppub_column_names = [
    "POOL_ID", "LOAN_ID", "ACT_PERIOD", "CHANNEL", "SELLER", "SERVICER",
    "MASTER_SERVICER", "ORIG_RATE", "CURR_RATE", "ORIG_UPB", "ISSUANCE_UPB",
    "CURRENT_UPB", "ORIG_TERM", "ORIG_DATE", "FIRST_PAY", "LOAN_AGE",
    "REM_MONTHS", "ADJ_REM_MONTHS", "MATR_DT", "OLTV", "OCLTV",
    "NUM_BO", "DTI", "CSCORE_B", "CSCORE_C", "FIRST_FLAG", "PURPOSE",
    "PROP", "NO_UNITS", "OCC_STAT", "STATE", "MSA", "ZIP", "MI_PCT",
    "PRODUCT", "PPMT_FLG", "IO", "FIRST_PAY_IO", "MNTHS_TO_AMTZ_IO",
    "DLQ_STATUS", "PMT_HISTORY", "MOD_FLAG", "MI_CANCEL_FLAG", "Zero_Bal_Code",
    "ZB_DTE", "LAST_UPB", "RPRCH_DTE", "CURR_SCHD_PRNCPL", "TOT_SCHD_PRNCPL",
    "UNSCHD_PRNCPL_CURR", "LAST_PAID_INSTALLMENT_DATE", "FORECLOSURE_DATE",
    "DISPOSITION_DATE", "FORECLOSURE_COSTS", "PROPERTY_PRESERVATION_AND_REPAIR_COSTS",
    "ASSET_RECOVERY_COSTS", "MISCELLANEOUS_HOLDING_EXPENSES_AND_CREDITS",
    "ASSOCIATED_TAXES_FOR_HOLDING_PROPERTY", "NET_SALES_PROCEEDS",
    "CREDIT_ENHANCEMENT_PROCEEDS", "REPURCHASES_MAKE_WHOLE_PROCEEDS",
    "OTHER_FORECLOSURE_PROCEEDS", "NON_INTEREST_BEARING_UPB", "PRINCIPAL_FORGIVENESS_AMOUNT",
    "ORIGINAL_LIST_START_DATE", "ORIGINAL_LIST_PRICE", "CURRENT_LIST_START_DATE",
    "CURRENT_LIST_PRICE", "ISSUE_SCOREB", "ISSUE_SCOREC", "CURR_SCOREB",
    "CURR_SCOREC", "MI_TYPE", "SERV_IND", "CURRENT_PERIOD_MODIFICATION_LOSS_AMOUNT",
    "CUMULATIVE_MODIFICATION_LOSS_AMOUNT", "CURRENT_PERIOD_CREDIT_EVENT_NET_GAIN_OR_LOSS",
    "CUMULATIVE_CREDIT_EVENT_NET_GAIN_OR_LOSS", "HOMEREADY_PROGRAM_INDICATOR",
    "FORECLOSURE_PRINCIPAL_WRITE_OFF_AMOUNT", "RELOCATION_MORTGAGE_INDICATOR",
    "ZERO_BALANCE_CODE_CHANGE_DATE", "LOAN_HOLDBACK_INDICATOR", "LOAN_HOLDBACK_EFFECTIVE_DATE",
    "DELINQUENT_ACCRUED_INTEREST", "PROPERTY_INSPECTION_WAIVER_INDICATOR",
    "HIGH_BALANCE_LOAN_INDICATOR", "ARM_5_YR_INDICATOR", "ARM_PRODUCT_TYPE",
    "MONTHS_UNTIL_FIRST_PAYMENT_RESET", "MONTHS_BETWEEN_SUBSEQUENT_PAYMENT_RESET",
    "INTEREST_RATE_CHANGE_DATE", "PAYMENT_CHANGE_DATE", "ARM_INDEX",
    "ARM_CAP_STRUCTURE", "INITIAL_INTEREST_RATE_CAP", "PERIODIC_INTEREST_RATE_CAP",
    "LIFETIME_INTEREST_RATE_CAP", "MARGIN", "BALLOON_INDICATOR",
    "PLAN_NUMBER", "FORBEARANCE_INDICATOR", "HIGH_LOAN_TO_VALUE_HLTV_REFINANCE_OPTION_INDICATOR",
    "DEAL_NAME", "RE_PROCS_FLAG", "ADR_TYPE", "ADR_COUNT", "ADR_UPB", "PAYMENT_DEFERRAL_MOD_EVENT_FLAG", "INTEREST_BEARING_UPB"
]

# Define column data types as a dictionary
lppub_column_classes = {
    "POOL_ID": "string", "LOAN_ID": "string", "ACT_PERIOD": "string", "CHANNEL": "string", "SELLER": "string", 
    "SERVICER": "string", "MASTER_SERVICER": "string", "ORIG_RATE": "float64", "CURR_RATE": "float64",
    "ORIG_UPB": "float64", "ISSUANCE_UPB": "float64", "CURRENT_UPB": "float64", "ORIG_TERM": "float64", 
    "ORIG_DATE": "string", "FIRST_PAY": "string", "LOAN_AGE": "float64", "REM_MONTHS": "float64", 
    "ADJ_REM_MONTHS": "float64", "MATR_DT": "string", "OLTV": "float64", "OCLTV": "float64", 
    "NUM_BO": "string", "DTI": "float64", "CSCORE_B": "float64", "CSCORE_C": "float64", "FIRST_FLAG": "string", 
    "PURPOSE": "string", "PROP": "string", "NO_UNITS": "float64", "OCC_STAT": "string", "STATE": "string", 
    "MSA": "string", "ZIP": "string", "MI_PCT": "float64", "PRODUCT": "string", "PPMT_FLG": "string", 
    "IO": "string", "FIRST_PAY_IO": "string", "MNTHS_TO_AMTZ_IO": "float64", "DLQ_STATUS": "string", 
    "PMT_HISTORY": "string", "MOD_FLAG": "string", "MI_CANCEL_FLAG": "string", "Zero_Bal_Code": "string", 
    "ZB_DTE": "string", "LAST_UPB": "float64", "RPRCH_DTE": "string", "CURR_SCHD_PRNCPL": "float64", 
    "TOT_SCHD_PRNCPL": "float64", "UNSCHD_PRNCPL_CURR": "float64", "LAST_PAID_INSTALLMENT_DATE": "string", 
    "FORECLOSURE_DATE": "string", "DISPOSITION_DATE": "string", "FORECLOSURE_COSTS": "float64", 
    "PROPERTY_PRESERVATION_AND_REPAIR_COSTS": "float64", "ASSET_RECOVERY_COSTS": "float64", 
    "MISCELLANEOUS_HOLDING_EXPENSES_AND_CREDITS": "float64", "ASSOCIATED_TAXES_FOR_HOLDING_PROPERTY": "float64", 
    "NET_SALES_PROCEEDS": "float64", "CREDIT_ENHANCEMENT_PROCEEDS": "float64", 
    "REPURCHASES_MAKE_WHOLE_PROCEEDS": "float64", "OTHER_FORECLOSURE_PROCEEDS": "float64", 
    "NON_INTEREST_BEARING_UPB": "float64", "PRINCIPAL_FORGIVENESS_AMOUNT": "float64", 
    "ORIGINAL_LIST_START_DATE": "string", "ORIGINAL_LIST_PRICE": "float64", "CURRENT_LIST_START_DATE": "string", 
    "CURRENT_LIST_PRICE": "float64", "ISSUE_SCOREB": "float64", "ISSUE_SCOREC": "float64", "CURR_SCOREB": "float64", 
    "CURR_SCOREC": "float64", "MI_TYPE": "string", "SERV_IND": "string", 
    "CURRENT_PERIOD_MODIFICATION_LOSS_AMOUNT": "float64", "CUMULATIVE_MODIFICATION_LOSS_AMOUNT": "float64", 
    "CURRENT_PERIOD_CREDIT_EVENT_NET_GAIN_OR_LOSS": "float64", "CUMULATIVE_CREDIT_EVENT_NET_GAIN_OR_LOSS": "float64", 
    "HOMEREADY_PROGRAM_INDICATOR": "string", "FORECLOSURE_PRINCIPAL_WRITE_OFF_AMOUNT": "float64", 
    "RELOCATION_MORTGAGE_INDICATOR": "string", "ZERO_BALANCE_CODE_CHANGE_DATE": "string", 
    "LOAN_HOLDBACK_INDICATOR": "string", "LOAN_HOLDBACK_EFFECTIVE_DATE": "string", "DELINQUENT_ACCRUED_INTEREST": "float64", 
    "PROPERTY_INSPECTION_WAIVER_INDICATOR": "string", "HIGH_BALANCE_LOAN_INDICATOR": "string", 
    "ARM_5_YR_INDICATOR": "string", "ARM_PRODUCT_TYPE": "string", "MONTHS_UNTIL_FIRST_PAYMENT_RESET": "float64", 
    "MONTHS_BETWEEN_SUBSEQUENT_PAYMENT_RESET": "float64", "INTEREST_RATE_CHANGE_DATE": "string", 
    "PAYMENT_CHANGE_DATE": "string", "ARM_INDEX": "string", "ARM_CAP_STRUCTURE": "string", 
    "INITIAL_INTEREST_RATE_CAP": "float64", "PERIODIC_INTEREST_RATE_CAP": "float64", 
    "LIFETIME_INTEREST_RATE_CAP": "float64", "MARGIN": "float64", "BALLOON_INDICATOR": "string", 
    "PLAN_NUMBER": "string", "FORBEARANCE_INDICATOR": "string", "HIGH_LOAN_TO_VALUE_HLTV_REFINANCE_OPTION_INDICATOR": "string", 
    "DEAL_NAME": "string", "RE_PROCS_FLAG": "string", "ADR_TYPE": "string", "ADR_COUNT": "float64", 
    "ADR_UPB": "float64", "PAYMENT_DEFERRAL_MOD_EVENT_FLAG": "string", "INTEREST_BEARING_UPB": "float64"
}

# Below are functions for processing data and cleaning
def load_and_concat_csv(file_path, column_names, column_classes, chunk_size=100000):
    """
    Loads a pipe-delimited CSV file in chunks and concatenates it into a single DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.
    - column_names (list): List of column names to assign to the DataFrame.
    - column_classes (dict): Dictionary specifying the data types for each column.
    - chunk_size (int): Number of rows to read at a time. Default is 100,000.

    Returns:
    - pd.DataFrame: Concatenated DataFrame containing all the data.
    """
    result = []

    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, sep='|', names=column_names, chunksize=chunk_size, dtype=column_classes):
        result.append(chunk)

    # Concatenate all chunks into a single DataFrame
    df = pd.concat(result, ignore_index=True)
    return df

def drop_na_columns(df):
    threshold = 0.8 * len(df)
    df = df.dropna(axis=1, thresh=threshold)
    return df

def classify_seller(seller_name):
    if pd.isna(seller_name):
        return 'Other'
    # Convert to lowercase for consistent matching
    seller_name = seller_name.lower()

    # Define keywords for each seller category
    bank_keywords = [
        'bank', 'national association', 'credit union', 'fifth third', 
        'pnc', 'citizens', 'wells fargo', 'regions', 
        'suntrust', 'truist', 'jpmorgan', 'citi'
    ]
    
    mortgage_company_keywords = [
        'mortgage', 'lending', 'loan', 'servicing', 'financial', 
        'loandepot', 'pennymac', 'roundpoint', 
        'freedom', 'quicken', 'amerihome', 'guild', 'caliber'
    ]
    
    investor_keywords = [
        'trust', 'real estate investment trust', 'investment', 
        'fund', 'capital', 'group', 'acquisition'
    ]

    # Classification logic based on keywords
    if any(keyword in seller_name for keyword in bank_keywords):
        return 'Bank'
    elif any(keyword in seller_name for keyword in mortgage_company_keywords):
        return 'Mortgage Company'
    elif any(keyword in seller_name for keyword in investor_keywords):
        return 'Investor'
    else:
        return 'Other'
    
def classify_servicer_type(seller_name):
    if pd.isna(seller_name):
        return 'Other' 
    # Convert to lowercase for consistent matching
    seller_name = seller_name.lower()
    
    # Define keywords for each category
    bank_keywords = [
        'bank', 'national association', 'credit union', 'fifth third', 
        'pnc', 'citizens bank', 'wells fargo', 'regions bank', 
        'suntrust', 'truist', 'jpmorgan', 'citi'
    ]
    
    mortgage_company_keywords = [
        'mortgage', 'lending', 'loan', 'servicing', 'financial', 
        'homeloans', 'loandepot', 'pennymac', 'roundpoint', 
        'freedom', 'quicken', 'amerihome', 'guild', 'caliber'
    ]
    
    # Check for keywords in the seller name
    if any(keyword in seller_name for keyword in bank_keywords):
        return 'Bank'
    elif any(keyword in seller_name for keyword in mortgage_company_keywords):
        return 'Mortgage Company'
    else:
        return 'Other'


def process_data(df):
    columns = ['LOAN_ID', 'ACT_PERIOD', 'original_rate', 'orginal_credit_score', 'original_loan_to_value', 'curr_unpaid',
    'seller_type', 'servicer_type', 'channel_type', 'adjusted_remaining_time', 
    'num_borrowers', 'purpose', 'property_type', 'occupancy_status', 'state', 
    'default_status', 'mod_indicator', 
    'homeready_indicator', 'relocation_mortgage_indicator', 
    'high_balance_loan_indicator', 'htlv_indicator', 
    'payment_deferral'
    ]

    # Orginal Rate
    df['original_rate'] = df['ORIG_RATE']
    # Credit Score
    df['orginal_credit_score'] = df['CSCORE_B']
    # Original loan to value ratio
    df['original_loan_to_value'] = df['OLTV']

    df['curr_unpaid'] = df['CURRENT_UPB']
    # ['Mortgage Company' 'Other' 'Bank' 'Investor']
    df['seller_type'] = df['SELLER'].apply(classify_seller)
    # ['Mortgage Company' 'Other' 'Bank']
    df['servicer_type'] = df['SERVICER'].apply(classify_servicer_type)

    channel_map = {'C': 0, 'B': 1, 'R': 2}
    df['channel_type'] = df['CHANNEL'].map(channel_map)

    df['adjusted_remaining_time'] = df['ADJ_REM_MONTHS'] / df['ORIG_TERM']

    df['num_borrowers'] = pd.to_numeric(df['NUM_BO'], errors='coerce')

    df['purpose'] = df['PURPOSE'].map({'P': 0, 'C': 1, 'R': 1, 'U': 1})

    prop_map = {'SF': 0, 'PU': 1, 'CO': 2, 'MH': 3, 'CP': 4}
    df['property_type'] = df['PROP'].map(prop_map)

    occupancy_map = {'U': 0, 'P': 1, 'I': 2, 'S': 3}
    df['occupancy_status'] = df['OCC_STAT'].map(occupancy_map)

    states = ['GA', 'KS', 'IL', 'IN', 'TX', 'UT', 'MO', 'IA', 'OR', 'DE', 'CA', 'MI', 'KY',
          'CO', 'NY', 'PA', 'WI', 'WA', 'VA', 'AZ', 'MD', 'TN', 'MA', 'OH', 'SC', 'AK',
          'AL', 'LA', 'MN', 'NC', 'AR', 'MS', 'OK', 'NE', 'NJ', 'ID', 'FL', 'ND', 'NV',
          'NM', 'CT', 'VT', 'WV', 'DC', 'ME', 'SD', 'NH', 'MT', 'HI', 'PR', 'RI', 'WY',
          'VI', 'GU']
    state_mapping = {state: idx + 1 for idx, state in enumerate(sorted(states))}
    df['state'] = df['STATE'].map(state_mapping)

    # [0: no default, 1: 30-59days, 2: 60-89 days, 3: 90-119 days, 4: 120-149 days, 5: 150-179 days, 6: 180-209 days]
    df['default_status'] = pd.to_numeric(df['DLQ_STATUS'], errors='coerce').fillna(0)

    df['mod_indicator'] = df['MOD_FLAG'].map({'N': 0, 'Y': 1}).fillna(0)

    df['homeready_indicator'] = df['HOMEREADY_PROGRAM_INDICATOR'].map({'7': 0, 'F': 1, 'H': 2})

    df['relocation_mortgage_indicator'] = df['RELOCATION_MORTGAGE_INDICATOR'].map({'N': 0, 'Y': 1})

    df['high_balance_loan_indicator'] = df['HIGH_BALANCE_LOAN_INDICATOR'].map({'N': 0, 'Y': 1})

    df['htlv_indicator'] = df['HIGH_LOAN_TO_VALUE_HLTV_REFINANCE_OPTION_INDICATOR'].map({'N': 0, 'Y': 1})

    df['payment_deferral'] = df['PAYMENT_DEFERRAL_MOD_EVENT_FLAG'].map({'N': 0, 'Y': 1,'7': 2})

    
    return df[columns]  # Return the processed DataFrame

def add_y_label(df):
    df['ACT_PERIOD'] = pd.to_datetime(df['ACT_PERIOD'].astype(str), format='%m%Y')
    df['y_label'] = 0
    # For each loan, we check the next 8 quarters' DLQ_STATUS
    for loan_id, group in df.groupby('LOAN_ID'):
        for i in range(len(group)):
            # Get the current row
            current_row = group.iloc[i]
            
            # Get the next 8 quarters' DLQ_STATUS (or until the end of the group)
            next_quarters = group.iloc[i + 1:i + 25] if i + 25 <= len(group) else group.iloc[i + 1:]
            
            # If any of the next quarters' DLQ_STATUS is >= 3, set y_label to 1
            if any(next_quarters['default_status'] >= 3):
                df.loc[current_row.name, 'y_label'] = 1
    return df

def save_output(df, original_file_path, new_directory):
    original_filename = os.path.basename(original_file_path)
    new_file_path = os.path.join(new_directory, original_filename)
    df.to_csv(new_file_path, index=False)
    print(f"Processed data saved to: {new_file_path}")
    
def run(original_file_path, new_directory):
    print("Loading CSV data...")
    df = load_and_concat_csv(original_file_path, lppub_column_names, lppub_column_classes)

    # 2. Process the data (cleaning and transformations)
    print("Processing data...")
    df = process_data(df)

    # 3. Save the processed data to a new CSV file in the specified directory
    print("Saving processed data...")
    save_output(df, original_file_path, new_directory)
    return df


