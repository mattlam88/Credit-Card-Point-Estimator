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
        username TEXT,
        brand TEXT,
        creditCardType TEXT, 
        rewardType TEXT,
        restaurantMultiplier INTEGER,
        groceryMultiplier INTEGER,
        nonCategoryMultiplier INTEGER,
        utilityMultiplier INTEGER,
        gasMultiplier INTEGER,
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
        maxRestaurantMultiplier INTEGER,
        maxGroceryMultiplier INTEGER,
        maxNonCategoryMultiplier INTEGER,
        maxUtilityMultiplier INTEGER,
        maxGasMultiplier INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE monthlyBudget (
        id INTEGER PRIMARY KEY,
        username TEXT,
        month TEXT
        year INTEGER,
        restaurantSpend INTEGER,
        grocerySpend INTEGER,
        nonCategorySpend INTEGER,
        utilitySpend INTEGER,
        gasSpend INTEGER,
        monthlySpend INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE yearlyBudget (
        id INTEGER PRIMARY KEY,
        username TEXT,
        year INTEGER,
        restaurantSpendYearly INTEGER,
        grocerySpendYearly INTEGER,
        nonCategorySpendYearly INTEGER,
        utilitySpendYearly INTEGER,
        gasSpendYearly INTEGER,
        yearlySpend INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE rewardPoints (
        id INTEGER PRIMARY KEY,
        username TEXT,
        year INTEGER,
        rewardType TEXT,
        janPoints INTEGER,
        febPoints INTEGER,
        marPoints INTEGER,
        aprPoints INTEGER,
        mayPoints INTEGER,
        junPoints INTEGER,
        julPoints INTEGER,
        augPoints INTEGER,
        sepPoints INTEGER,
        octPoints INTEGER,
        novPoints INTEGER,
        decPoints INTEGER,
        totalYearPoints INTEGER,
        pointsFMV INTEGER
    );
    """
)

c.execute(
    """
    CREATE TABLE rewardPointsEV (
        id INTEGER PRIMARY KEY,
        rewardType TEXT,
        expectedValue INTEGER
    );
    """
)

conn.commit()
c.close()

print("Looks like we're all good to go!")
