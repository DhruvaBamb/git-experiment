#!/usr/bin/env python3
"""
Simple runner for the Object Recognition ML Project
Run this file to execute the complete demonstration.
"""

if __name__ == "__main__":
    print("🚀 Starting Object Recognition ML Project...")
    print("   This may take a few minutes to complete...")

    try:
        from main_project import main
        results = main()
        print("\n✅ Project completed successfully!")
        print("   Check the generated files for detailed results.")
    except Exception as e:
        print(f"❌ Error running project: {e}")
        print("   Please ensure all dependencies are installed:")
        print("   pip install tensorflow opencv-python matplotlib seaborn numpy pandas pillow scikit-learn")
