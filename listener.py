import html

def style_first_lines_safe(text: str) -> str:
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    formatted_paragraphs = []
    
    # Ограничиваем пост максимум 2-3 абзацами, чтобы он был коротким
    max_paragraphs = min(len(paragraphs), 3)
    
    for i in range(max_paragraphs):
        p = paragraphs[i]
        escaped_p = html.escape(p)
        
        parts = escaped_p.split(". ", 1)
        if len(parts) > 1 and len(parts[0]) < 50:
            # Делаем первые слова жирными и подчеркнутыми одновременно
            formatted_p = f"<b><u>{parts[0]}.</u></b> {parts[1]}"
        else:
            words = escaped_p.split()
            if len(words) > 4:
                bold_part = " ".join(words[:4])
                rest_part = " ".join(words[4:])
                formatted_p = f"<b><u>{bold_part}</u></b> {rest_part}"
            else:
                formatted_p = f"<b><u>{escaped_p}</u></b>"
                
        formatted_paragraphs.append(formatted_p)
        
    return "\n\n".join(formatted_paragraphs)
