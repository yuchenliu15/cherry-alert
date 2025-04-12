import EmailForm from "@/components/email-form"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 md:p-24">
      <div className="w-full max-w-2xl space-y-8 text-center">
        <div className="space-y-8">
          <h1 className="text-4xl font-bold tracking-tight md:text-5xl">🌸 Sign up for cherry alert! 🌸</h1>
          <p className="text-lg text-muted-foreground">Stay updated with the latest cherry blossoms at Brooklyn Botanic Garden.</p>
        </div>
        <EmailForm />
      </div>
    </main>
  )
}
