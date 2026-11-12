(() => {
  const fieldSelector = 'input:not([type="hidden"]):not([type="submit"]):not([type="button"]):not([type="reset"]), select, textarea';

  const fieldNames = {
    name: 'Full name',
    fullname: 'Full name',
    full_name: 'Full name',
    phone: 'Mobile or WhatsApp number',
    mobile: 'Mobile or WhatsApp number',
    email: 'Email address',
    company: 'Company or unit name',
    company_name: 'Company or unit name',
    companyname: 'Company or unit name',
    location: 'Area in Pune',
    city: 'City or area in Pune',
    locality: 'Area in Pune',
    bill: 'Monthly electricity bill',
    monthly_bill: 'Monthly electricity bill',
    billrange: 'Monthly electricity bill',
    system_type: 'System type',
    service: 'Service required',
    requirement: 'Service required',
    propertytype: 'Property type',
    property_type: 'Property type',
    propertystyle: 'Property type',
    propertycategory: 'Property type',
    sector: 'Business sector',
    midc_zone: 'MIDC zone',
    shed_area: 'Approximate shed area',
    capacity: 'System capacity',
    plant_capacity: 'Existing system capacity',
    system_size: 'Solar system size',
    inverter_brand: 'Inverter brand and model',
    msedcl_consumer_no: 'MSEDCL consumer number',
    existing_capacity: 'Existing plant capacity',
    plant_history: 'Plant history and goals',
    fault_description: 'Fault description',
    error_details: 'Issue details',
    dispute_details: 'Dispute details',
    contractdemand: 'Contract demand',
    phase: 'MIDC phase',
    message: 'Project details'
  };

  const humanize = (value) => value
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
    .replace(/[_-]+/g, ' ')
    .replace(/\b\w/g, (letter) => letter.toUpperCase());

  const labelFor = (control) => {
    const key = (control.name || control.id || '').toLowerCase();
    if (fieldNames[key]) return fieldNames[key];
    if (control.placeholder) {
      return control.placeholder
        .replace(/^e\.g\.?\s*/i, '')
        .replace(/\s*\*\s*$/, '')
        .trim();
    }
    return humanize(control.name || control.id || 'Project detail');
  };

  const uniqueId = (control, index) => {
    if (control.id) return control.id;
    const base = `ui-form-field-${index + 1}`;
    let id = base;
    let suffix = 2;
    while (document.getElementById(id)) id = `${base}-${suffix++}`;
    control.id = id;
    return id;
  };

  const findFieldWrapper = (control, form) => {
    let node = control.parentElement;
    while (node && node !== form) {
      const fields = node.querySelectorAll(fieldSelector);
      if (fields.length === 1) return node;
      node = node.parentElement;
    }
    return null;
  };

  const addLabel = (control, wrapper, index) => {
    const id = uniqueId(control, index);
    let label = control.labels && control.labels.length ? control.labels[0] : null;
    if (!label && wrapper) label = wrapper.querySelector('label');

    if (!wrapper) {
      wrapper = document.createElement('div');
      wrapper.className = 'ui-form-field';
      control.parentNode.insertBefore(wrapper, control);
      wrapper.appendChild(control);
    } else {
      wrapper.classList.add('ui-form-field');
    }

    if (!label) {
      label = document.createElement('label');
      label.className = 'ui-field-label';
      label.htmlFor = id;
      label.textContent = labelFor(control);
      wrapper.insertBefore(label, control);
    } else {
      label.classList.add('ui-field-label');
      label.htmlFor = id;
    }

    const labelText = label.textContent || '';
    if (control.required && !labelText.includes('*')) {
      const required = document.createElement('span');
      required.className = 'ui-field-required';
      required.setAttribute('aria-hidden', 'true');
      required.textContent = '*';
      label.appendChild(required);
    } else if (!control.required && !/optional/i.test(labelText)) {
      const optional = document.createElement('span');
      optional.className = 'ui-field-optional';
      optional.textContent = 'Optional';
      label.appendChild(optional);
    }

    if (control.tagName === 'TEXTAREA' || /message|details|history|description/i.test(control.name || '')) {
      wrapper.classList.add('ui-form-field--wide');
    }

    if (control.type === 'tel' && !control.autocomplete) control.autocomplete = 'tel';
    if (control.type === 'email' && !control.autocomplete) control.autocomplete = 'email';
    if (/^(name|fullname|full_name)$/i.test(control.name || '') && !control.autocomplete) {
      control.autocomplete = 'name';
    }
  };

  const enhanceForms = () => {
    document.querySelectorAll('form').forEach((form) => {
      form.classList.add('ui-form-enhanced');
      const fields = Array.from(form.querySelectorAll(fieldSelector));
      fields.forEach((control, index) => {
        addLabel(control, findFieldWrapper(control, form), index);
      });

      Array.from(form.querySelectorAll('button')).filter((button) => button.type === 'submit')
        .concat(Array.from(form.querySelectorAll('input[type="submit"]')))
        .forEach((button) => {
          button.classList.add('ui-form-submit');
        });

      const setColumnLayout = () => {
        const narrow = form.getBoundingClientRect().width > 0 && form.getBoundingClientRect().width < 560;
        form.classList.toggle('ui-form-narrow', narrow);
      };
      setColumnLayout();
      if ('ResizeObserver' in window) {
        new ResizeObserver(setColumnLayout).observe(form);
      }
    });
  };

  const tableName = (table) => {
    const caption = table.querySelector('caption');
    if (caption && caption.textContent.trim()) return caption.textContent.trim();
    const columns = table.querySelectorAll('thead th').length || table.querySelectorAll('tr:first-child th, tr:first-child td').length;
    return columns ? `Data table with ${columns} columns` : 'Scrollable data table';
  };

  const enhanceTables = () => {
    document.querySelectorAll('table').forEach((table) => {
      table.querySelectorAll('thead th').forEach((heading) => {
        if (!heading.hasAttribute('scope')) heading.setAttribute('scope', 'col');
      });
      table.querySelectorAll('tbody tr th:first-child').forEach((heading) => {
        if (!heading.hasAttribute('scope')) heading.setAttribute('scope', 'row');
      });

      let region = table.closest('.dt-table-wrap, .ui-table-scroll');
      if (!region) {
        region = document.createElement('div');
        region.className = 'ui-table-scroll';
        table.parentNode.insertBefore(region, table);
        region.appendChild(table);
      }
      region.setAttribute('role', 'region');
      region.setAttribute('aria-label', `${tableName(table)}. Scroll horizontally to view all columns.`);
      region.setAttribute('tabindex', '0');
    });
  };

  const run = () => {
    enhanceForms();
    enhanceTables();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run, { once: true });
  } else {
    run();
  }
})();
