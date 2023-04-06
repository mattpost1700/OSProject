{{- define "app1.image" -}}
  image: "{{ .Values.image.repository }}-{{ .Values.appName }}:{{ .Values.image.tag }}"
  imagePullPolicy: {{ .Values.image.pullPolicy }}
{{- end -}}
