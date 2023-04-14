import customtkinter as ctk

class UpscalerGUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Upscalify')
        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('dark-blue')
        # Left Frame
        left_frame = ctk.CTkFrame(self)
        left_frame.pack(side='left')


        # Upscale Type Selection
        upscale_type_lbl = ctk.CTkLabel(left_frame, text='Upscale Type')
        upscale_type_lbl.pack()
        upscale_type_var = ctk.StringVar()
        upscale_type_var.set('REAL-ESGRAN')
        upscale_type_chk = ctk.CTkOptionMenu(left_frame, values=('REALSR', 'REMACRI', 'ULTRAMIX-BALANCED', 'ULTRASHARP', 'DIGITAL ART'), variable=upscale_type_var)
        upscale_type_chk.pack()


        # Upscale Rate Selection
        upscale_rate_lbl = ctk.CTkLabel(left_frame, text='Upscale Rate')
        upscale_rate_lbl.pack()
        upscale_2x_var = ctk.BooleanVar()
        upscale_4x_var = ctk.BooleanVar()
        upscale_8x_var = ctk.BooleanVar()
        upscale_2x_chk = ctk.CTkCheckBox(left_frame, text='2x', variable=upscale_2x_var)
        upscale_2x_chk.pack()
        upscale_4x_chk = ctk.CTkCheckBox(left_frame, text='4x', variable=upscale_4x_var)
        upscale_4x_chk.pack()
        upscale_8x_chk = ctk.CTkCheckBox(left_frame, text='8x', variable=upscale_8x_var)
        upscale_8x_chk.pack()

        # Output Folder Selection
        output_folder_lbl = ctk.CTkLabel(left_frame, text='Output Folder')
        output_folder_lbl.pack()
        output_folder_btn = ctk.CTkButton(left_frame, text='Select Folder')
        output_folder_btn.pack()

        # Start Button
        start_btn = ctk.CTkButton(left_frame, text='Start')
        start_btn.pack()

        # Right Frame
        right_frame = ctk.CTkFrame(self)
        right_frame.pack(side='right', padx=10, pady=10)

        # Image Preview
        image_preview_lbl = ctk.CTkLabel(right_frame, text='Image Preview')
        image_preview_lbl.pack()
        image_preview_canvas = ctk.CTkCanvas(right_frame, width=256, height=256, bg='grey')
        image_preview_canvas.pack()

if __name__ == '__main__':
    app = UpscalerGUI()
    app.mainloop()