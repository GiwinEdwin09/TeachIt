import reflex as rx
from components.navbar import Navbar

# class MyHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         """Serve the form for the contact page."""
#         if self.path == "/": 
#             self.path = "/templates/index.html"
#         else:
#             self.path = self.path
        
#         return SimpleHTTPRequestHandler.do_GET(self)

#     def do_POST(self):
#         """Handle the form submission."""
#         if self.path == "/submit_form":
#             content_length = int(self.headers['Content-Length'])
#             post_data = self.rfile.read(content_length).decode('utf-8')
#             post_params = parse.parse_qs(post_data)
            
#             # Extract form data
#             name = post_params.get('name', [''])[0]
#             email = post_params.get('email', [''])[0]
#             message = post_params.get('message', [''])[0]

#             # Display the submitted information
#             self.send_response(200)
#             self.send_header('Content-type', 'text/html')
#             self.end_headers()

#             # Render the display page with the user's input
#             with open("templates/display.html", "r") as f:
#                 display_page = f.read()
            
#             # Inject user data into the display page
#             display_page = display_page.format(name=name, email=email, message=message)
#             self.wfile.write(display_page.encode())

# def run(server_class=HTTPServer, handler_class=MyHandler):
#     """Run the HTTP server."""
#     server_address = (HOST, PORT)
#     httpd = server_class(server_address, handler_class)
#     print(f"Serving on {HOST}:{PORT}")
#     httpd.serve_forever()

# if __name__ == "__main__":
#     run()

import reflex as rx
font_style = ("Helvetica", 16, "bold"),

# Create a label with custom font
   
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)



def contact_page() -> rx.Component:
    return rx.box(rx.vstack(
        rx.center(rx.text("Contact", font_family="IBM Plex Mono", font_size="3em", width="200px")),
        # rx.text("Contact us here!", font_family="IBM Plex Mono", font_size="2em"),
        # You can style the section here if needed
        # style={"background": "#f9fafb", "padding": "6rem 0", "position": "relative"},
        rx.text("Questions? Feel free to reach out!", font_family="IBM Plex Mono", font_size="2em", width="800px"),
        rx.text("epardhe@asu.edu", font_family="IBM Plex Mono", font_size="2em", width="800px"),
        rx.text("edwin.giwin@gmail.com", font_family="IBM Plex Mono", font_size="2em", width="800px")
    ),
    text_align="center"
    )
#rx.flex(
    rx.center(rx.text("Example"), bg="lightblue"),
    rx.spacer(),

@rx.page(route="/contact")
def contact():
    return rx.container(
        Navbar(),
        contact_page()
    )
