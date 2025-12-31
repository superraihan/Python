import pandas as pd

# Sample data
world = pd.DataFrame({
    'name': ['China', 'USA', 'Brazil', 'Nepal', 'India'],
    'population': [1400000000, 331000000, 212000000, 30000000, 1380000000],
    'area': [9600000, 9830000, 8510000, 147000, 3287000]
})

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    ans = world.loc[
        (world['area'] >= 3000000) | (world['population'] >= 25000000),
        ['name', 'population', 'area']
    ]
    return ans

# ✅ Call the function and print the result
result = big_countries(world)
print(result)
