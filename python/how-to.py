def paper_airplane():
    steps = [
        "1. Start with a rectangular piece of paper.",
        "2. Fold the paper in half lengthwise, then unfold.",
        "3. Fold the top corners to the center crease to form a triangle.",
        "4. Fold the new top edges to the center crease again.",
        "5. Fold the plane in half along the original crease.",
        "6. Fold down the wings so they align with the bottom edge of the plane.",
        "7. Your paper airplane is complete!"
    ]
    return steps

def paper_snowflake():
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper in half diagonally to form a triangle.",
        "3. Fold the triangle in half again to form a smaller triangle.",
        "4. Fold the triangle into thirds, overlapping the edges.",
        "5. Cut various shapes along the edges.",
        "6. Unfold the paper to reveal your snowflake!"
    ]
    return steps

def paper_lantern():
    steps = [
        "1. Start with a rectangular piece of paper.",
        "2. Fold the paper in half lengthwise.",
        "3. Cut slits along the fold, stopping about an inch from the edge.",
        "4. Unfold the paper and roll it into a cylinder.",
        "5. Tape or glue the edges together.",
        "6. Attach a handle at the top, and your paper lantern is complete!"
    ]
    return steps

def paper_flowers():
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper in half diagonally to form a triangle.",
        "3. Fold the left and right corners to meet the top corner.",
        "4. Fold the bottom corner up to the top.",
        "5. Cut the paper into a petal shape.",
        "6. Unfold the paper to reveal a flower. Repeat for more flowers!"
    ]
    return steps

def origami_bird():
    steps = [
        "1. Start with a square piece of paper, color side up.",
        "2. Fold the paper in half diagonally to form a triangle, then unfold.",
        "3. Fold the paper diagonally in the other direction, forming a smaller triangle.",
        "4. Fold the left and right corners of the triangle to meet at the top point, forming a diamond shape.",
        "5. Fold the top layer of the bottom point up to the top point.",
        "6. Flip the paper over and repeat on the other side.",
        "7. Fold the wings down, and your origami bird is complete!"
    ]
    return steps

def origami_fish():
    steps = [
        "1. Start with a square piece of paper, color side up.",
        "2. Fold the paper in half diagonally to form a triangle, then unfold.",
        "3. Fold the paper diagonally in the other direction, forming a smaller triangle.",
        "4. Fold the left and right corners of the triangle to meet at the top point, forming a diamond shape.",
        "5. Flip the paper over and fold the bottom point up to meet the top point, creating a smaller triangle.",
        "6. Fold the left and right corners up to the top point again.",
        "7. Fold the small triangles at the top back down to form fins.",
        "8. Fold the bottom point up slightly to form the fish’s mouth.",
        "9. Add details like eyes with a pen or marker, and your origami fish is complete!"
    ]
    return steps

def main():
    print("Welcome! What would you like to make?")
    print("1. Paper Airplane")
    print("2. Paper Snowflake")
    print("3. Paper Lantern")
    print("4. Paper Flowers")
    print("5. Origami Bird")
    print("6. Origami Fish")
    
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
    elif choice == "6":
        instructions = origami_fish()
    else:
        print("Invalid choice. Please select a number from 1 to 6.")
        return
    
    print("\nHere are the instructions:")
    for step in instructions:
        print(step)
    
if __name__ == "__main__":
    main()
