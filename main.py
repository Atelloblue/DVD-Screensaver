from scene import *

# --- Constants ---
LOGO_FILENAME = 'dvd_logo.png'  # Your image filename
INITIAL_X = 100
INITIAL_Y = 100
SPEED_X = 4
SPEED_Y = 4
LOGO_WIDTH = 250  # Set a fixed width
LOGO_HEIGHT = 250  # Set a fixed height

class BouncingLogo(Scene):
    def setup(self):
        self.logo_filename = LOGO_FILENAME  # Store the filename string
        self.valid_image = False  # Flag to check if image loaded successfully

        # Attempt to load texture primarily to get size and check for errors
        try:
            temp_texture = Texture(self.logo_filename)
            logo_width, logo_height = temp_texture.size
            self.valid_image = True
        except Exception as e:
            print(f"Error loading image '{self.logo_filename}': {e}")
            print("Please ensure the image file exists and is accessible.")
            # Use fallback dimensions if loading failed
            logo_width, logo_height = LOGO_WIDTH, LOGO_HEIGHT  # Use fixed size

        # Create the bounds Rect using the fixed logo size
        self.bounds = Rect(INITIAL_X, INITIAL_Y, LOGO_WIDTH, LOGO_HEIGHT)

        # Set speed only if the image was valid
        if self.valid_image:
            self.dx = SPEED_X
            self.dy = SPEED_Y
        else:
            self.dx = 0
            self.dy = 0

    def update(self):
        # Don't move if the image wasn't loaded correctly
        if not self.valid_image:
            return

        # Move the logo's bounds
        self.bounds.x += self.dx
        self.bounds.y += self.dy

        # Get screen dimensions
        screen_width = self.size.w
        screen_height = self.size.h

        # Bounce off edges using the bounds Rect
        # Horizontal bounce
        if self.bounds.x <= 0 or (self.bounds.x + self.bounds.width) >= screen_width:
            self.dx = -self.dx
            # Optional: Clamp position
            if self.bounds.x < 0: self.bounds.x = 0
            elif (self.bounds.x + self.bounds.width) > screen_width: self.bounds.x = screen_width - self.bounds.width

        # Vertical bounce
        if self.bounds.y <= 0 or (self.bounds.y + self.bounds.height) >= screen_height:
            self.dy = -self.dy
            # Optional: Clamp position
            if self.bounds.y < 0: self.bounds.y = 0
            elif (self.bounds.y + self.bounds.height) > screen_height: self.bounds.y = screen_height - self.bounds.height

    def draw(self):
        # Set background to black
        background(0, 0, 0)

        # Draw based on whether the image was successfully processed in setup
        if self.valid_image:
            # --- Key Change Here ---
            # Pass the FILENAME STRING to the image() function
            image(self.logo_filename,
                  self.bounds.x,
                  self.bounds.y,
                  self.bounds.width,
                  self.bounds.height)
        else:
             # Draw error placeholder if image failed in setup
             fill(1,0,0)  # Red
             # Center the error text (alignment=5 is center in scene's text)
             try:
                 text('Image Error', font_name='Helvetica', font_size=16, x=self.size.w/2, y=self.size.h/2, alignment=5)
             except Exception:  # Fallback if text arguments are different
                 text('Image Error', x=self.size.w/2, y=self.size.h/2)


# Run the scene
run(BouncingLogo(), PORTRAIT)
