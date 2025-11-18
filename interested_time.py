import pandas as pd

df = pd.read_csv("altitude_velocity_acceleration_30s.csv")
df["Time (s)"] = df["Timestamp"] - df["Timestamp"].iloc[0]

# Selected time 9600s ~ 10050s
df_range = df[(df["Time (s)"] >= 9600) & (df["Time (s)"] <= 10050)].copy()

df_range["tracking_error"] = 33000 - df_range["Altitude"]
df_range["tracking_error_derivative"] = -df_range["V_vertical"]
df_range["tracking_error_second_derivative"] = -df_range["A_vertical"]

result = df_range[["Time (s)", "tracking_error", "tracking_error_derivative", "tracking_error_second_derivative"]]

result.to_csv("tracking_error_dynamics_9600s_to_10050s.csv", index=False)