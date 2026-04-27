def analyze_data(df):
    print("\n📊 ANALYSIS REPORT")
    print("------------------")

    print("Total clients:", df["client"].nunique())
    print("Total revenue:", df["montant"].sum())

    print("\nRevenue by project type:")
    print(df.groupby("type_projet")["montant"].sum())