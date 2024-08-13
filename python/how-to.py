def paper_airplane():
    steps = [
        "1. Start with a rectangular piece of paper, like a standard 8.5 x 11 inch sheet.",
        "2. Fold the paper in half lengthwise and then unfold it. This will leave you with a crease in the center.",
        "3. Fold the top two corners down towards the center crease, making a triangle at the top.",
        "4. Fold the angled edges towards the center crease again, forming a sharper point at the top.",
        "5. Fold the entire paper in half along the original center crease, keeping all folds inside.",
        "6. Fold the wings down by folding each side down to align with the bottom edge of the plane.",
        "7. Adjust the wings so that they’re even and flat. Your paper airplane is ready to fly!"
    ]
    return steps

def paper_snowflake():
    steps = [
        "1. Start with a square piece of paper. If you have a rectangular sheet, cut it to make it square.",
        "2. Fold the paper diagonally in half to form a triangle.",
        "3. Fold the triangle in half again to form a smaller triangle.",
        "4. Fold the triangle into thirds. This is the trickiest part, but try to get the folds as even as possible.",
        "5. Cut off the top of the triangle so you have a straight edge.",
        "6. Now, cut various shapes out of the edges of the paper. Be creative!",
        "7. Carefully unfold the paper to reveal your unique snowflake!"
    ]
    return steps

def main():
    print("Welcome! What would you like to make?")
    print("1. Paper Airplane")
    print("2. Paper Snowflake")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        instructions = paper_airplane()
    elif choice == "2":
        instructions = paper_snowflake()
    else:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    print("\nHere are the instructions:")
    for step in instructions:
        print(step)
    
if __name__ == "__main__":
    main()
