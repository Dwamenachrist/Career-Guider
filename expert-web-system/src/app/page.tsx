"use client"

import { useState } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Badge } from "@/components/ui/badge"
import { Loader2, BriefcaseIcon, BookOpenIcon, AwardIcon, AlertCircle } from "lucide-react"
import { motion, AnimatePresence } from "framer-motion"

export default function CareerExpertSystem() {
  const [skills, setSkills] = useState("")
  const [interests, setInterests] = useState("")
  const [education, setEducation] = useState("Bachelor's Degree")
  const [recommendations, setRecommendations] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setError(null)
    setRecommendations([])

    try {
      const response = await fetch("http://localhost:5000/api/recommendations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          skills: skills.split(",").map((s) => s.trim()),
          interests: interests.split(",").map((i) => i.trim()),
          education,
        }),
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      setRecommendations(data)
    } catch (error) {
      console.error("Error fetching recommendations:", error)
      setError("Failed to fetch recommendations. Please check your backend.")
    } finally {
      setIsLoading(false)
    }
  }

  return (
      <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
        <div className="container mx-auto px-4 py-16">
          <Card className="max-w-2xl mx-auto">
            <CardHeader>
              <CardTitle className="text-3xl font-bold text-center flex items-center justify-center gap-2">
                <BriefcaseIcon className="h-8 w-8 text-primary" />
                Career Path Expert System
              </CardTitle>
              <CardDescription className="text-center text-lg mt-2">
                Discover your ideal career path based on your skills, interests, and education
              </CardDescription>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="space-y-2">
                  <label htmlFor="skills" className="text-sm font-medium">
                    Skills
                  </label>
                  <Input
                      id="skills"
                      placeholder="e.g., programming, problem-solving, communication"
                      value={skills}
                      onChange={(e) => setSkills(e.target.value)}
                      className="w-full"
                  />
                  <p className="text-sm text-muted-foreground">Enter your skills separated by commas</p>
                </div>

                <div className="space-y-2">
                  <label htmlFor="interests" className="text-sm font-medium">
                    Interests
                  </label>
                  <Input
                      id="interests"
                      placeholder="e.g., technology, science, art"
                      value={interests}
                      onChange={(e) => setInterests(e.target.value)}
                      className="w-full"
                  />
                  <p className="text-sm text-muted-foreground">Enter your interests separated by commas</p>
                </div>

                <div className="space-y-2">
                  <label htmlFor="education" className="text-sm font-medium">
                    Education Level
                  </label>
                  <Select value={education} onValueChange={setEducation}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select education level" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="High School">High School</SelectItem>
                      <SelectItem value="Associate's Degree">Associate's Degree</SelectItem>
                      <SelectItem value="Bachelor's Degree">Bachelor's Degree</SelectItem>
                      <SelectItem value="Master's Degree">Master's Degree</SelectItem>
                      <SelectItem value="Juris Doctor">Juris Doctor</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <Button type="submit" className="w-full" disabled={isLoading || !skills || !interests}>
                  {isLoading ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        Analyzing your profile...
                      </>
                  ) : (
                      "Get Career Recommendations"
                  )}
                </Button>
              </form>

              <AnimatePresence>
                {error && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className="mt-6"
                    >
                      <Alert variant="destructive">
                        <AlertCircle className="h-4 w-4" />
                        <AlertTitle>Error</AlertTitle>
                        <AlertDescription>{error}</AlertDescription>
                      </Alert>
                    </motion.div>
                )}

                {recommendations.length > 0 && (
                    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mt-8 space-y-6">
                      <h2 className="text-2xl font-bold flex items-center gap-2">
                        <AwardIcon className="h-6 w-6 text-primary" />
                        Your Career Recommendations
                      </h2>
                      <div className="grid gap-4">
                        {recommendations.map((career, index) => (
                            <motion.div
                                key={career.title}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: index * 0.1 }}
                            >
                              <Card>
                                <CardHeader>
                                  <CardTitle className="text-xl flex items-center gap-2">
                                    <BookOpenIcon className="h-5 w-5 text-primary" />
                                    {career.title}
                                  </CardTitle>
                                </CardHeader>
                                <CardContent className="space-y-4">
                                  <p className="text-muted-foreground">{career.description}</p>
                                  <div className="space-y-2">
                                    <h4 className="font-medium">Required Qualifications:</h4>
                                    <div className="flex flex-wrap gap-2">
                                      {career.qualifications.split(",").map((qual, i) => (
                                          <Badge key={i} variant="secondary">
                                            {qual.trim()}
                                          </Badge>
                                      ))}
                                    </div>
                                  </div>
                                </CardContent>
                              </Card>
                            </motion.div>
                        ))}
                      </div>
                    </motion.div>
                )}
              </AnimatePresence>
            </CardContent>
          </Card>
        </div>
      </div>
  )
}

