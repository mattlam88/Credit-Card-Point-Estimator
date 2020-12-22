import sqlite3

conn = sqlite3.connect("creditCard.db")
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS creditCardDetails;""")
c.execute("""DROP TABLE IF EXISTS users;""")
c.execute("""DROP TABLE IF EXISTS monthlyBudget;""")
c.execute("""DROP TABLE IF EXISTS yearlyBudget;""")
c.execute("""DROP TABLE IF EXISTS rewardPoints;""")

c.execute(
    """
    CREATE TABLE creditCardDetails (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        creditCardType TEXT, 
        rewardType TEXT,
        restaurantMultiplier INTEGER,
        groceryMultiplier INTEGER,
        nonCategoryMultiplier INTEGER,
        utilityMultiplier INTEGER,
        gasMultiplier INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        username TEXT,
        password BLOB,
        creditCardOneID INTEGER,
        creditCardTwoID INTEGER,
        creditCardThreeID INTEGER,
        budgetID INTEGER,
        creditCardOnePointsTotal INTEGER,
        creditCardTwoPointsTotal INTEGER,
        creditCardThreePointsTotal INTEGER,
        creditCardOnePointsFMV INTEGER,
        creditCardTwoPointsFMV INTEGER,
        creditCardThreePointsFMV INTEGER

    );
    """
)

c.execute(
    """
    CREATE TABLE monthlyBudget (
        id INTEGER PRIMARY KEY,
        username TEXT,
        month TEXT,
        restaurantSpend INTEGER,
        grocerySpend INTEGER,
        nonCategorySpend INTEGER,
        utilitySpend INTEGER,
        gasSpend INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE yearlyBudget (
        id INTEGER PRIMARY KEY,
        username TEXT,
        janSpendTotal INTEGER,
        janPointsTotal INTEGER,
        febSpendTotal INTEGER,
        febPointsTotal INTEGER,
        marSpendTotal INTEGER,
        marPointsTotal INTEGER,
        aprSpendTotal INTEGER,
        aprPointsTotal INTEGER,
        maySpendTotal INTEGER,
        mayPointsTotal INTEGER,
        juneSpendTotal INTEGER,
        junePointsTotal INTEGER,
        julySpendTotal INTEGER,
        julyPointsTotal INTEGER,
        augSpendTotal INTEGER,
        augPointsTotal INTEGER,
        septSpendTotal INTEGER,
        septPointsTotal INTEGER,
        octSpendTotal INTEGER,
        octPointsTotal INTEGER,
        novSpendTotal INTEGER,
        novPointsTotal INTEGER,
        decSpendTotal INTEGER,
        decPointsTotal INTEGER,
        yearlySpendTotal INTEGER,
        yearlyPointsTotal INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE rewardPoints (
        id INTEGER PRIMARY KEY,
        rewardType TEXT,
        expectedValue INTEGER
    );
    """
)

conn.commit()
c.close()

print("Looks like we're all good to go!")
