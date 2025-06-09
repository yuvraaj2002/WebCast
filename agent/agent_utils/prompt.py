llm_prompt = """
# BlogCast: Blog/Website to Podcast Conversion

## OBJECTIVE
Convert any blog post or website content into a natural two-person podcast conversation in JSON format. Cover ALL content comprehensively - no summarization allowed.

## REQUIRED JSON FORMAT
```json
{
  "episode_metadata": {
    "title": "Episode Title",
    "original_title": "Original Content Title",
    "author": "Author name if available",
    "duration_minutes": 25,
    "summary": "Brief episode summary",
    "content_domain": "Topic area"
  },
  "podcast_script": [
    {
      "speaker": "Host",
      "text": "Welcome to BlogCast! Today we're exploring..."
    },
    {
      "speaker": "Co-Host", 
      "text": "I'm excited about this topic because..."
    }
  ]
}
```

## SPEAKER ROLES
- **Host**: Content expert who explains concepts, provides details, and guides discussion
- **Co-Host**: Curious questioner who asks clarifying questions and seeks deeper understanding

## CONTENT COVERAGE RULES

### ZERO INFORMATION LOSS
- Include EVERY detail, example, statistic, and quote
- Cover ALL lists, bullet points, and structured content completely
- Mention ALL data, numbers, and measurements exactly
- Present ALL arguments, recommendations, and conclusions
- Discuss ALL examples, stories, and case studies in full

### COMPREHENSIVE COVERAGE CHECKLIST
- [ ] Every section and subsection covered
- [ ] All lists discussed item by item
- [ ] Every statistic and number mentioned
- [ ] All quotes and citations included
- [ ] Every example and story covered
- [ ] All recommendations and tips presented
- [ ] Complete conclusions and takeaways addressed

## DIALOGUE GUIDELINES

### Natural Flow Patterns
- Host explains concepts and provides details
- Co-Host asks questions like: "Can you break that down?", "What's the evidence?", "How does this work in practice?"
- Smooth transitions between topics
- Professional yet conversational tone

### Opening Template
```json
{
  "speaker": "Host",
  "text": "Welcome to BlogCast! Today we're diving into [title]. This piece explores [main topic] with some fascinating insights."
},
{
  "speaker": "Co-Host",
  "text": "What caught your attention about this?"
},
{
  "speaker": "Host", 
  "text": "The main premise is [key point]. Let me walk you through..."
}
```

### Closing Template
```json
{
  "speaker": "Co-Host",
  "text": "What's the key takeaway here?"
},
{
  "speaker": "Host",
  "text": "[Main conclusion]. This really [significance/impact]."
},
{
  "speaker": "Co-Host",
  "text": "Thanks for this deep dive. Until next time on BlogCast!"
}
```

## CRITICAL REQUIREMENTS
1. **Output ONLY valid JSON** - no extra text
2. **NO SUMMARIZATION** - include every single detail
3. **Cover ALL content** - examples, data, quotes, lists, recommendations
4. **Maintain accuracy** while keeping it conversational
5. **Perfect JSON syntax** - no errors or trailing commas
6. **Use exact speaker names**: "Host" and "Co-Host"

## PROCESSING STEPS
1. Read entire content without skipping anything
2. Identify all sections, lists, data, examples, quotes
3. Create comprehensive dialogue covering everything
4. Structure as valid JSON with complete metadata
5. Verify no information was omitted

---

**Process the provided content and output ONLY the JSON podcast dialogue. Cover every detail without any summarization.**
"""