"""
===========================================================
Project : BIM Wall Name Validator
Version : 1.0
Author  : Hamad Ali

Description:
This Python script opens an IFC model, reads all wall
elements (IfcWall), validates their names, and reports
the first invalid wall found.

Validation Rules:
- Wall name must not be empty.
- Wall name must not be None.
- Wall name must not be "Unknown".

Technologies:
- Python 3
- IfcOpenShell
- IFC (Industry Foundation Classes)

===========================================================
"""

# ==========================================================
# Import Required Library
# ==========================================================

import ifcopenshell


# ==========================================================
# IFC File Path
# ==========================================================

IFC_FILE_PATH = r"C:\Users\Hamad Ali\Documents\scit lab\BIM\Snowdon.ifc"


# ==========================================================
# Main Program
# ==========================================================

print("=" * 55)
print("        BIM Wall Name Validator")
print("=" * 55)

print("\nLoading IFC model...\n")

try:
    # Open IFC Model
    ifc_file = ifcopenshell.open(IFC_FILE_PATH)
    print("✔ IFC model loaded successfully.\n")

except Exception as error:
    print("❌ Error loading IFC model.")
    print(error)
    exit()


# ==========================================================
# Read All Walls
# ==========================================================

walls = ifc_file.by_type("IfcWall")

print(f"Total Walls Found : {len(walls)}\n")

print("Validating wall names...\n")


# ==========================================================
# Validate Wall Names
# ==========================================================

for wall in walls:

    wall_name = wall.Name

    if (
        wall_name is None
        or wall_name == ""
        or wall_name == "Unknown"
    ):

        print("=" * 55)
        print("❌ INVALID WALL FOUND")
        print("=" * 55)

        print(f"Global ID : {wall.GlobalId}")
        print(f"Wall Name : {wall_name}")

        print("\nValidation Stopped.")
        break

else:

    print("=" * 55)
    print("✅ VALIDATION COMPLETED")
    print("=" * 55)

    print("All wall names are valid.")


print("\nProgram Finished.")