"use client"

import { useState } from "react"
import axios from "axios"

export default function UploadForm() {

  const [file, setFile] = useState<File | null>(null)
  const [result, setResult] = useState<any>(null)

  const submit = async () => {

    if (!file) return

    const form = new FormData()
    form.append("file", file)

    const res = await axios.post("/api/scan", form)

    setResult(res.data)
  }

  return (
    <div>

      <input
        type="file"
        accept="image/*"
        capture="environment"
        onChange={(e)=>setFile(e.target.files?.[0] || null)}
      />

      <button onClick={submit}>
        Scan
      </button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}

    </div>
  )
}
