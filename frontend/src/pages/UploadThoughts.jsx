<div className="container">
  <h1>Upload Your Excel File</h1>
  <form id="file-upload-form" encType="multipart/form-data">
    <div className="form-group">
      <label htmlFor="excel-file">Excel File</label>
      <input type="file" className="form-control" id="excel-file" name="excel-file" accept=".xlsx, .xls" />
    </div>
    <div className="form-group">
      <label htmlFor="title">Title</label>
      <input type="text" className="form-control" id="title" name="title" placeholder="Title" required />
    </div>
    <div className="form-group">
      <label htmlFor="description">Description</label>
      <textarea className="form-control" id="description" name="description" placeholder="Description" required></textarea>
    </div>
    <div className="form-group">
      <label htmlFor="category">Category</label>
      <select className="form-control" id="category" name="category" required>
        <option value="">Select Category</option>
        <option value="tech">Tech</option>
        <option value="science">Science</option>
        <option value="math">Math</option>
        <option value="literature">Literature</option>
      </select>
    </div>
    <button type="submit" className="btn btn-primary">Upload File</button>
  </form>
  <div id="uploaded-files-list">
    {/* Uploaded files will be listed here */}
  </div>
</div>
