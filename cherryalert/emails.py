import resend
import os
from .processing import CherryInfo
import logging
import dotenv
dotenv.load_dotenv()

def send(to_email: list[str], cherry: CherryInfo):
	resend.api_key = os.getenv("RESEND_API")
	resend.Emails.send({
      "from": "onboarding@resend.dev",
      "to": to_email,
      "subject": f"🌸 {cherry.blossom_percentage:.2f}% blooming! 🌸",
      "html": 
        f"<p><strong>Blooming cherries: {cherry.blossoms}</strong><br>"
        f"Yet to bloomb: {cherry.no_blossoms}</p>"
    })
	logging.info(f"Sent email to {to_email} with cherry data: {cherry}")

if __name__ == '__main__':
	dotenv.load_dotenv()
	send(["eugeneliuosm@gmail.com"], CherryInfo(no_blossoms=9, blossoms=20))
