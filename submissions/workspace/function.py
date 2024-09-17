import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def update_production_with_prediction(production, new_prediction, time_steps=7):
    """Update production DataFrame with new predictions and maintain a rolling window."""
    new_row = pd.DataFrame(new_prediction, columns=['Oil production cumulative', 'Gas production cumulative', 'Water production cumulative'])
    production = pd.concat([production, new_row], ignore_index=True)

    if len(production) > time_steps + 1:
        production = production.iloc[1:].reset_index(drop=True)
    
    return production

def preprocess_data(state, production, time_steps=7):

    mean_vector = state.mean().values

    # Create lag features
    production['oil_production_lag_1'] = production['Oil production cumulative'].shift(1)
    production['oil_production_lag_3'] = production['Oil production cumulative'].shift(3)
    production['oil_production_lag_7'] = production['Oil production cumulative'].shift(7)

    production['water_production_lag_1'] = production['Water production cumulative'].shift(1)
    production['water_production_lag_3'] = production['Water production cumulative'].shift(3)
    production['water_production_lag_7'] = production['Water production cumulative'].shift(7)

    production['gas_production_lag_1'] = production['Gas production cumulative'].shift(1)
    production['gas_production_lag_3'] = production['Gas production cumulative'].shift(3)
    production['gas_production_lag_7'] = production['Gas production cumulative'].shift(7)

    # Drop rows with NaN values (created due to shifting)
    production = production.dropna(ignore_index=True)

    # Create a DataFrame from the mean vector
    df_mean = pd.DataFrame([mean_vector], columns=['mean_X', 'mean_Y', 'mean_Depth', 'mean_permeabilityX', 'mean_permeabilityY', 'mean_permeabilityZ', 'mean_porosity', 'mean_transmissibility'])

    # Merge the production data with the mean vector
    # Since df_mean contains only one row, we need to broadcast it to match df_production's number of rows
    df_mean_broadcasted = pd.concat([df_mean] * len(production), ignore_index=True)
    df_merged = pd.concat([production, df_mean_broadcasted], axis=1)

    # Prepare features and targets, including the 'day' column separately
    X = df_merged.drop(columns=['Oil production cumulative', 'Gas production cumulative', 'Water production cumulative'])
    y = df_merged[['Oil production cumulative', 'Gas production cumulative', 'Water production cumulative']]

    # Normalize the features
    scaler_X = StandardScaler()
    X_scaled = scaler_X.fit_transform(X)

    # Normalize the targets
    scaler_y = StandardScaler()
    y_scaled = scaler_y.fit_transform(y)

    # Create sequences
    def create_sequences(X, y, time_steps):
        X_seq, y_seq = [], []
        for i in range(len(X) - time_steps + 1):
            X_seq.append(X[i:i + time_steps])
            y_seq.append(y[i + time_steps - 1])
        return np.array(X_seq), np.array(y_seq)

    X_sequences, y_sequences = create_sequences(X_scaled, y_scaled, time_steps)

    return X_sequences, y_sequences, X_scaled, y_scaled, scaler_X, scaler_y
