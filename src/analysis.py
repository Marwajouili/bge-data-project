def analyze_data(df):
    print("\n📊 ANALYSIS REPORT")
    print("-------------------")

    # KPI 1 : nombre de clients uniques
    print("👥 Total clients:", df["client"].nunique())

    # KPI 2 : revenu total
    print("💰 Total revenue:", df["montant"].sum())

    # KPI 3 : moyenne des montants
    print("📊 Average project value:", df["montant"].mean())

    # KPI 4 : par région
    print("\n🌍 Revenue by region:")
    print(df.groupby("region")["montant"].sum())

    # KPI 5 : par type de projet
    print("\n📁 Revenue by project type:")
    print(df.groupby("type_projet")["montant"].sum())