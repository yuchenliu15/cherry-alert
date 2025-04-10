import resend
import dotenv
import os
from .task import CherryImage

dotenv.load_dotenv()
resend.api_key = os.getenv("RESEND_API")

def send(to_email: list[str], cherry: CherryImage):
    resend.Emails.send({
      "from": "onboarding@resend.dev",
      "to": to_email,
      "subject": f"🌸 {cherry.blossom_percentage:.2f}% blooming! 🌸",
      "html": 
        f"<p><strong>Blooming cherries: {cherry.blossoms}</strong><br>"
        f"Yet to bloomb: {cherry.no_blossoms}</p>"
    })

if __name__ == '__main__':
    send(["eugeneliuosm@gmail.com"], CherryImage(no_blossoms=9, blossoms=20))
