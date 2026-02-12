# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for day_record in data:
        sales = day_record[product_key]
        total += sales
        
    return total
    


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = 0
    average = 0 
    for day_record in data:
        sales = day_record[product_key]
        total += sales
    average = total/20
    return average


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    best_day_sales = 0
    highest_day = 0
    max_sales = 0
    for sales in data:
        highest_day = sales["product_a"] + sales["product_b"] + sales["product_c"]
        if max_sales < highest_day:
            max_sales = highest_day
            best_day_sales = sales["day"]
    return best_day_sales


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    day_exceed_threshold = []
    day_aux = 0
    count = 0
    for exceed in data:
        day_aux = exceed[product_key]
        if day_aux > threshold:
            count += 1
            day_exceed_threshold.append(exceed["day"])
    return count


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    pro_a = 0
    pro_b = 0
    pro_c = 0
    for item in data:
        pro_a += item["product_a"]
        pro_b += item["product_b"]
        pro_c += item["product_c"]
    
    if pro_a > pro_b and pro_a > pro_c:
        return "product_a"
    if pro_b > pro_a and pro_b > pro_c:
        return "product_b"
    if pro_c > pro_b and pro_c > pro_a:
        return "product_a"         

def Worst_day_sales(data):
    min_sales = 100000
    the_worst_day = 0
    for sales in data:
        daily_total = sales["product_a"] + sales["product_b"] + sales["product_c"]
        if min_sales > daily_total:
           min_sales = daily_total
           the_worst_day = sales["day"]
    return the_worst_day

def top_3_sales_days(data):
    ranking = []
    
    for day_record in data:
        total = day_record["product_a"] + day_record["product_b"] + day_record["product_c"]
        ranking.append((total, day_record["day"]))
    
    ranking.sort(reverse=True)
    
    return ranking[:3]

def calculate_sales_range(data, product_key):
    max_sales = 0
    min_sales = 10000
    
    for day_record in data:
        sales = day_record[product_key]
        
        if sales > max_sales:
            max_sales = sales
            
        if sales < min_sales:
            min_sales = sales
            
    return max_sales - min_sales

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Day with the worst sales:", Worst_day_sales(sales_data))
print("the days by total sales and show the top 3:", top_3_sales_days(sales_data))
print("the range (maximum - minimum) of the sales of a product:", calculate_sales_range(sales_data, "product_a"))
