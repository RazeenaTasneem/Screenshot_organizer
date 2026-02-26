import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def show_popup(image_path, suggested_name, suggested_category):
    """
    Displays a Tkinter popup patterned after the Windows "Low Battery" system dialog.
    Returns a dictionary: {"confirmed": bool, "name": str, "category": str}
    """
    root = tk.Tk()
    root.title("Screenshot Captured")
    
    window_width = 360
    window_height = 210
    
    # Remove standard borders to look like a native Metro/Windows 10 popup
    root.overrideredirect(True)
    
    # Keep on top and centered
    root.attributes("-topmost", True)
    root.focus_force()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Position bottom right with margins (20px right, 60px bottom for taskbar)
    x_cordinate = int(screen_width - window_width - 20)
    y_cordinate = int(screen_height - window_height - 60)
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    bg_color = "#1F1F1F"
    fg_color = "#FFFFFF"
    font_large = ("Segoe UI", 10, "bold")
    font_normal = ("Segoe UI", 8, "normal")
    font_small = ("Segoe UI", 8, "normal")
    
    result = {
        "confirmed": False,
        "name": suggested_name,
        "category": suggested_category
    }

    # Accent color border (mimics system accent color box)
    border_frame = tk.Frame(root, bg="#0078D7", bd=1)
    border_frame.pack(fill=tk.BOTH, expand=True)
    
    main_frame = tk.Frame(border_frame, bg=bg_color)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # ------------------
    # HEADER (Low battery style)
    # ------------------
    header_frame = tk.Frame(main_frame, bg=bg_color)
    header_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
    
    # Yellow triangle / battery icon
    lbl_icon = tk.Label(header_frame, text="📷", font=("Segoe UI Emoji", 16), bg=bg_color, fg="#FFFFFF")
    lbl_icon.pack(side=tk.LEFT, padx=(0, 5))
    
    # Title imitating "Your battery is running low."
    text_frame = tk.Frame(header_frame, bg=bg_color)
    text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    lbl_title = tk.Label(text_frame, text="Screenshot captured.", font=font_large, bg=bg_color, fg=fg_color)
    lbl_title.pack(anchor="w")
    
    # Subtitle imitating "You might want to plug in your PC."
    lbl_desc = tk.Label(text_frame, text="Confirm details.", font=font_normal, bg=bg_color, fg="#CCCCCC")
    lbl_desc.pack(anchor="w")

    # ------------------
    # BODY CONTENT (Image Left, Inputs Right)
    # ------------------
    body_frame = tk.Frame(main_frame, bg=bg_color)
    body_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    # Left side: Image Preview
    preview_frame = tk.Frame(body_frame, bg=bg_color)
    preview_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 10))
    
    try:
        img = Image.open(image_path)
        img.thumbnail((140, 90))
        photo = ImageTk.PhotoImage(img)
        lbl_img = tk.Label(preview_frame, image=photo, bg=bg_color)
        lbl_img.image = photo
        lbl_img.pack()
    except Exception as e:
        tk.Label(preview_frame, text="[ No Image ]", font=font_normal, bg=bg_color, fg="#777777").pack()

    # Right side: Inputs
    input_frame = tk.Frame(body_frame, bg=bg_color)
    input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
    
    tk.Label(input_frame, text="Name", font=font_small, bg=bg_color, fg=fg_color).pack(anchor="w", pady=(0, 2))
    entry_name = tk.Entry(input_frame, font=font_normal, relief=tk.SOLID, bd=1, highlightthickness=1, highlightcolor="#0078D7", highlightbackground="#555555", bg="#333333", fg="#FFFFFF", insertbackground="#FFFFFF")
    entry_name.insert(0, suggested_name)
    entry_name.pack(fill=tk.X, pady=(0, 6), ipady=2)
    
    tk.Label(input_frame, text="Folder", font=font_small, bg=bg_color, fg=fg_color).pack(anchor="w", pady=(0, 2))
    entry_category = tk.Entry(input_frame, font=font_normal, relief=tk.SOLID, bd=1, highlightthickness=1, highlightcolor="#0078D7", highlightbackground="#555555", bg="#333333", fg="#FFFFFF", insertbackground="#FFFFFF")
    entry_category.insert(0, suggested_category)
    entry_category.pack(fill=tk.X, pady=(0, 2), ipady=2)

    # ------------------
    # FOOTER / BUTTONS (Like Window's grey action area)
    # ------------------
    footer_frame = tk.Frame(border_frame, bg="#2B2B2B", height=55)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
    footer_frame.pack_propagate(False)
    
    def on_save():
        result["confirmed"] = True
        result["name"] = entry_name.get()
        result["category"] = entry_category.get()
        root.destroy()
        
    def on_cancel():
        root.destroy()
        
    def on_enter(e, widget, color):
        widget['background'] = color

    def on_leave(e, widget, color):
        widget['background'] = color
        
    font_button = ("Segoe UI", 10, "bold")
        
    # Blue primary button
    btn_save = tk.Button(footer_frame, text="Save", command=on_save, bg="#0078D7", fg="#FFFFFF", font=font_button, relief=tk.FLAT, width=12, cursor="hand2")
    btn_save.bind("<Enter>", lambda e: on_enter(e, btn_save, "#005A9E"))
    btn_save.bind("<Leave>", lambda e: on_leave(e, btn_save, "#0078D7"))
    btn_save.pack(side=tk.RIGHT, padx=(10, 15), pady=12)
    
    # Grey secondary button
    btn_cancel = tk.Button(footer_frame, text="Cancel", command=on_cancel, bg="#CCCCCC", fg="#000000", font=font_button, relief=tk.FLAT, width=12, cursor="hand2")
    btn_cancel.bind("<Enter>", lambda e: on_enter(e, btn_cancel, "#BBBBBB"))
    btn_cancel.bind("<Leave>", lambda e: on_leave(e, btn_cancel, "#CCCCCC"))
    btn_cancel.pack(side=tk.RIGHT, pady=12)

    # Key bindings
    root.bind('<Return>', lambda event: on_save())
    root.bind('<Escape>', lambda event: on_cancel())
    
    root.mainloop()
    return result

