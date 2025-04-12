"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { subscribeEmail } from "@/lib/actions"

export default function EmailForm() {
  const [email, setEmail] = useState("")
  const [status, setStatus] = useState<{ message: string; type: "success" | "error" } | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!email || !email.includes("@")) {
      setStatus({
        message: "Please enter a valid email address",
        type: "error",
      })
      return
    }

    setIsSubmitting(true)
    setStatus(null)

    try {
      const result = await subscribeEmail(email)

      if (result.success) {
        setStatus({
          message: "Thank you for subscribing!",
          type: "success",
        })
        setEmail("")
      } else {
        setStatus({
          message: result.error || "Something went wrong. Please try again.",
          type: "error",
        })
      }
    } catch (error) {
      setStatus({
        message: "Something went wrong. Please try again.",
        type: "error",
      })
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="space-y-4">
      <form onSubmit={handleSubmit} className="flex w-full space-x-2">
        <Input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="flex-1"
          disabled={isSubmitting}
          required
        />
        <Button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Subscribing..." : "Subscribe"}
        </Button>
      </form>

      {status && (
        <div className={`text-sm ${status.type === "success" ? "text-green-600" : "text-red-600"}`} role="alert">
          {status.message}
        </div>
      )}
    </div>
  )
}
