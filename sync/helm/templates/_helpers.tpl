{{- define "sync.resources" -}}
{{- range $v := .Values.resources }}
{{ $v | toYaml }}
{{- end }}
{{- end -}}
