# Odoo 19 Custom Modules
# Extends official image for CI/CD

FROM odoo:19.0

# Copy all modules from repo root
COPY . /mnt/extra-addons

# If you have additional Python dependencies, uncomment:
# USER root
# RUN pip3 install --no-cache-dir --break-system-packages -r /mnt/extra-addons/requirements.txt
# USER odoo