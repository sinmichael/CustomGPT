import { NextApiRequest, NextApiResponse } from 'next'

export default async function createMessage(req: NextApiRequest, res: NextApiResponse) {
  const { messages } = req.body

  const url = `${process.env.API_HOST}?query=${messages[messages.length - 1].content}`

  try {
    const response = await fetch(url, {
      method: 'GET'
    })
    const data = await response.json()
    res.status(200).json({ data })
  } catch (error: any) {
    res.status(500).json({ error: error.message })
  }
}
