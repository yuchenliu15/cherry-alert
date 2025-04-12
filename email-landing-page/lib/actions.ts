"use server"

import { Redis } from "@upstash/redis"

// Initialize Redis client
const redis = new Redis({
  url: process.env.KV_REST_API_URL,
  token: process.env.KV_REST_API_TOKEN || "",
})

export async function subscribeEmail(email: string) {
  try {
    // Validate email format
    if (!email || !email.includes("@")) {
      return {
        success: false,
        error: "Please provide a valid email address",
      }
    }

    // Generate a unique ID for the subscription
    const timestamp = new Date().toISOString()
    const id = `email:${email}`

    // Check if email already exists
    const exists = await redis.exists(id)

    if (exists) {
      return {
        success: false,
        error: "This email is already subscribed",
      }
    }

    // Store email in Redis with timestamp
    await redis.set(id, { email, timestamp })

    // Also add to a list for easy retrieval of all emails
    await redis.sadd("all_subscribers", email)

    return {
      success: true,
    }
  } catch (error) {
    console.error("Error subscribing email:", error)
    return {
      success: false,
      error: "Failed to subscribe. Please try again later.",
    }
  }
}
