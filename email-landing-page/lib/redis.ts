import { Redis } from "@upstash/redis"

// This is a utility file to get a Redis client instance
// It can be used in other parts of the application if needed

export function getRedisClient() {
  return new Redis({
    url: process.env.REDIS_URL || process.env.KV_URL || "",
    token: process.env.KV_REST_API_TOKEN || "",
  })
}
