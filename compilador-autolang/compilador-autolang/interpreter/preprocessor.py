class PrePro:
    @staticmethod
    def filter(source):
        lines = source.split('\n')
        filtered_lines = []
        for line in lines:
            line = line.split('--')[0]  # Remove os comentários
            filtered_lines.append(line)
        return '\n'.join(filtered_lines)
