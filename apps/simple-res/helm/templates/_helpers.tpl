{{- define "simple-res.image" -}}
{{- printf "%s/%s:%s" .Values.image.registry .Release.Name .Values.image.tag | trimSuffix "-" -}}
{{- end -}}
