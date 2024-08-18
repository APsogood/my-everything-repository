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

def paper_lantern():
    steps = [
        "1. Start with a rectangular piece of paper.",
        "2. Fold the paper in half lengthwise.",
        "3. Cut slits along the folded edge, about 1 inch apart. Leave about 1 inch of uncut paper at the edges.",
        "4. Unfold the paper.",
        "5. Bring the long edges of the paper together to form a cylinder shape, with the slits running vertically.",
        "6. Secure the edges with tape or glue.",
        "7. Add a handle by attaching a strip of paper to the top. Your lantern is complete!"
    ]
    return steps

def paper_flowers():
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper in half diagonally to form a triangle.",
        "3. Fold the triangle in half again to form a smaller triangle.",
        "4. Fold the triangle in thirds, overlapping the sides slightly.",
        "5. Cut the top of the triangle into a rounded shape.",
        "6. Unfold the paper to reveal a flower shape.",
        "7. You can layer multiple flowers for a fuller effect or add a stem using a strip of green paper."
    ]
    return steps

def origami_bird():
    steps = [
        "1. Start with a square piece of paper, color side up.",
        "2. Fold the paper in half diagonally, then unfold.",
        "3. Fold the paper in half diagonally in the other direction, then unfold again. This will leave you with an X-shaped crease.",
        "4. Flip the paper over and fold it in half horizontally and vertically, then unfold. You now have creases that make a star shape.",
        "5. Collapse the paper along the creases into a smaller square with open flaps at the bottom.",
        "6. Fold the top layers of both sides to the center crease, creating a kite shape. Repeat on the other side.",
        "7. Fold the top point down on both sides, then unfold these folds.",
        "8. Reverse fold the sides to form the bird's head and tail.",
        "9. Fold the wings down, and your origami bird is complete!"
    ]
    return steps

def main():
    print("Welcome! What would you like to make?")
    print("1. Paper Airplane")
    print("2. Paper Snowflake")
    print("3. Paper Lantern")
    print("4. Paper Flowers")
    print("5. Origami Bird")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        instructions = paper_airplane()
    elif choice == "2":
        instructions = paper_snowflake()
    elif choice == "3":
        instructions = paper_lantern()
    elif choice == "4":
        instructions = paper_flowers()
    elif choice == "5":
        instructions = origami_bird()
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
        return
    
    print("\nHere are the instructions:")
    for step in instructions:
        print(step)
    
if __name__ == "__main__":
    main()
