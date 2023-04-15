import customtkinter as ctk
import os
from ctypes import windll


lastClickX = 0
lastClickY = 0





class UpscalerGUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Upscalify')
        self.geometry('470x450')
        self.overrideredirect(True)
        if "nt" == os.name:
            self.wm_iconbitmap(bitmap = "media\icon.ico")
        else:
            self.wm_iconbitmap(bitmap = "media\icon.xbm")
        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('dark-blue') 

        def SaveLastClickPos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y


        def Dragging(event):
            x, y = event.x - lastClickX + self.winfo_x(), event.y - lastClickY + self.winfo_y()
            self.geometry("+%s+%s" % (x , y))
        
        self.bind('<Button-1>', SaveLastClickPos)
        self.bind('<B1-Motion>', Dragging)

        GWL_EXSTYLE=-20
        WS_EX_TOOLWINDOW = 0x00000080

        def set_toolwindow(self):
            hwnd = windll.user32.GetParent(self.winfo_id())
            style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
            style = style | WS_EX_TOOLWINDOW
            res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
            # re-assert the new window style
            self.wm_withdraw()
            self.after(10, lambda: self.wm_deiconify())
        
        #top frame
        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky='nsew')

        # Left Frame
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Upscale Type Selection
        upscale_type_lbl = ctk.CTkLabel(left_frame, text='Upscale Type')
        upscale_type_lbl.grid(row=0, column=0, sticky='w', padx=10)
        upscale_type_var = ctk.StringVar()
        upscale_type_var.set('REAL-ESGRAN')
        upscale_type_chk = ctk.CTkOptionMenu(left_frame, values=('REALSR', 'REMACRI', 'ULTRAMIX-BALANCED', 'ULTRASHARP', 'DIGITAL ART'), variable=upscale_type_var)
        upscale_type_chk.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        # Upscale Rate Selection
        upscale_rate_lbl = ctk.CTkLabel(left_frame, text='Upscale Rate')
        upscale_rate_lbl.grid(row=2, column=0, sticky='w', padx=10)
        upscale_2x_var = ctk.BooleanVar()
        upscale_4x_var = ctk.BooleanVar()
        upscale_8x_var = ctk.BooleanVar()
        upscale_2x_chk = ctk.CTkCheckBox(left_frame, text='2x', variable=upscale_2x_var)
        upscale_2x_chk.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        upscale_4x_chk = ctk.CTkCheckBox(left_frame, text='4x', variable=upscale_4x_var)
        upscale_4x_chk.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        upscale_8x_chk = ctk.CTkCheckBox(left_frame, text='8x', variable=upscale_8x_var)
        upscale_8x_chk.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        # Output Folder Selection
        output_folder_lbl = ctk.CTkLabel(left_frame, text='Output Folder', padx=10)
        output_folder_lbl.grid(row=6, column=0, sticky='w')
        output_folder_btn = ctk.CTkButton(left_frame, text='Select Folder')
        output_folder_btn.grid(row=7, column=0, padx=10, pady=10, sticky='w')

        # Start Button
        start_btn = ctk.CTkButton(left_frame, text='Start')
        start_btn.grid(row=8, column=0, padx=10, pady=10, sticky='w')

        # Right Frame

        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=1, column=1, padx=0, pady=11, sticky='nsew')

        # Close Button
        close_btn = ctk.CTkButton(top_frame, text='X', width=20, height=20)
        close_btn.grid(row=0, column=2, padx=1, pady=1, sticky='ne')
        close_btn.bind('<Button-1>', lambda e: self.destroy())
        
        #maximize button
        maximize_btn = ctk.CTkButton(top_frame, text='🗖', width=20, height=20)
        maximize_btn.grid(row=0, column=1, padx=1, pady=1, sticky='ne')

        #minimize button
        minimize_btn = ctk.CTkButton(top_frame, text='-', width=20, height=20)
        minimize_btn.grid(row=0, column=0, padx=1, pady=1, sticky='ne')


 

        # Image Preview
        image_preview_lbl = ctk.CTkLabel(right_frame, text='Image Preview', padx=10)
        image_preview_lbl.grid(row=0, column=0, sticky='w')
        image_preview_canvas = ctk.CTkCanvas(right_frame, width=256, height=256, bg='grey')
        image_preview_canvas.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

if __name__ == '__main__':
    app = UpscalerGUI()
    app.mainloop()